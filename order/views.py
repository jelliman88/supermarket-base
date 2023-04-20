from django.shortcuts import render, redirect
import ast
from django.contrib.auth.models import User
from .models import Order
from parts.models import Part
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='/login')
def index(request):
    if request.POST:
        order_exists = request.POST.get('current-order')
        data = request.POST.getlist('part')
        save_order = request.POST.get('save')
        obj_list = []
        for i in data:
            obj_list.append(ast.literal_eval(i))
        user = User.objects.get(username=request.user)
        if order_exists:
            order = Order.objects.get(current_order=True, user=request.user)
        else:
            order = Order(user=user, json_data=str(obj_list))
        
        if not save_order:
            order.current_order = False
            order.date = timezone.now()

        order.json_data=str(obj_list)    
        order.save()
        return redirect('order:orders')
        
    current_order = Order.objects.values().filter(current_order=True, user=request.user)
    if current_order:
        parts = jsonToLiteral(current_order)
    else: 
        parts = []
    return render(request, 'order/index.html', {'parts': parts, 'current_order': current_order})

@login_required(login_url='/login')
def orders(request):
    user_filter = ''
    if request.user.is_superuser:
        users = User.objects.filter(~Q(id=1))
        if request.POST:
            user_filter = request.POST.get('user-filter')
            user_obj = User.objects.get(username=user_filter)
            orders = Order.objects.filter(current_order=False, user=user_obj.id)
        else:
            orders = Order.objects.filter(current_order=False)
    else:
        users = []
        user = str(request.user)
        if 'lead' in user:
            store = user[:-5]
            store_obj = User.objects.get(username=store)
            ids = [store_obj.id, request.user.id]
            orders = Order.objects.filter(user__in=ids).order_by('-date').values()
        else:
            orders = Order.objects.filter(user=request.user).order_by('-date').values()
    
    return render(request, 'order/orders.html', {'orders': orders, 'users': users, 'user_filter': user_filter})

@login_required(login_url='/login')
def order_detail(request, id):
    if request.POST:
        pk = request.POST.get('order-pk')
        status = request.POST.get('status')
        archive = request.POST.get('archive')
        print(archive)
        urgent = request.POST.get('urgent')
        print(urgent)
        obj = Order.objects.get(pk=pk)
        print(status)
        if archive:
            status = 'archive'
            obj.completed = status
            obj.save()
            return redirect('order:orders')
        elif urgent:
            obj.urgent = True
            obj.save()
            return redirect('order:orders')
        else:
            obj.urgent = False
            obj.completed = status
            obj.save()
            return redirect('order:orders')

      
    
    order = Order.objects.values().filter(pk=id)
    user_in_question = User.objects.get(id=order[0].get('user_id'))
    parts = jsonToLiteral(order)
    order_info = ast.literal_eval(order[0].get('json_data'))
    urgent = order[0].get('urgent')
    for part in parts:
        part.quantity = order_info[parts.index(part)].get('quantity')
    
    return render(request, 'order/order-detail.html', {'order': order, 'parts': parts, 'user_in_question': user_in_question, 'urgent': urgent})

@login_required(login_url='/login')
def archive(request):
    clear_archive = request.POST.get('clear-archive')
    if clear_archive:
        print('delete')
    else:
        user_filter = ''
        if request.POST:
            user_filter = request.POST.get('user-filter')
            user_obj = User.objects.get(username=user_filter)
            queryset = Order.objects.filter(completed='archive', user=user_obj.id).order_by('-date')
        else:
            queryset = Order.objects.filter(completed='archive').order_by('-date')
        orders = Paginator(queryset, 25)
        users = User.objects.all()
        page_number = request.GET.get('page')
        page_obj = orders.get_page(page_number)
        return render(request, 'order/archive.html', {'orders': page_obj, 'users': users, 'user_filter': user_filter})
#AJAX
"""
def ajax_submit_order(request):
    print('hello')
    order = decodeJavaScript(request.GET.get('order'))
    print(order)
    res = {
        msg: 'success',
    }
    return JsonResponse(res, safe=False)
"""

def jsonToLiteral(order):
    json_string = order[0].get('json_data')
    parts_literal = ast.literal_eval(json_string) 
    parts = []
    for part in parts_literal:
        obj = Part.objects.get(part_no=part['part_no'])
        obj.quantity = part.get('quantity')
        parts.append(obj)
    return parts

def decodeJavaScript(request):
    obj_as_string = request.body.decode("utf-8")
    return ast.literal_eval(obj_as_string)