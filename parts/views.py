from django.shortcuts import render, get_object_or_404, redirect
from .models import Part, ExcelSheet
from .forms import PartForm, UpdateUserForm, NewUserForm, LoginForm
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .sprays import *
from .tools import *
from order.models import Order


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html',{'form':LoginForm()})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    
        if user is None:
                return render(request, 'auth/login.html',{'form':LoginForm(),'error':'incorrect login details'})
        else:
            login(request, user)
            return redirect('order:orders')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('parts:login')

@login_required(login_url='/login')
def accounts(request):
    users = User.objects.all()
    return render(request, 'auth/accounts.html', {'users':users})

@login_required(login_url='/login')
def add_account(request):
    if request.method == 'GET':
        return render(request, 'auth/add-account.html', {'form':NewUserForm()})
    else:
        try:
            form = NewUserForm(request.POST)
            new_user = form.save()
            login(request, new_user)
            return redirect('parts:accounts')
        except ValueError:
            return render(request, 'auth/add-account.html', {'form':NewUserForm(), 'error':'invalid data'})

@login_required(login_url='/login')
def account_detail(request, id):
    if request.POST:
        user = get_object_or_404(User, id=id)
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('parts:accounts')
    user = get_object_or_404(User, id=id)
    form = UpdateUserForm(instance=user)
    return render(request, 'auth/account-detail.html', {'user':user, 'form':form})

@login_required(login_url='/login')
def listParts(request):
    search = request.GET.get('search')
    out_of_stock = request.GET.get('out-of-stock')
    inactive = request.GET.get('inactive')
    if search:
        try:
            sku = int(search)
            if out_of_stock:
                parts = Part.objects.filter(part_no__contains=sku, out_of_stock=True, inactive=False).order_by('part_no')
            else:
                parts = Part.objects.filter(part_no__contains=sku, inactive=False).order_by('part_no')
        except:
            if out_of_stock:
                parts = Part.objects.filter(title__contains=sku, out_of_stock=True, inactive=False).order_by('part_no')
            else:
                parts = Part.objects.filter(title__contains=search, inactive=False).order_by('part_no')
    else:
        if out_of_stock:
                parts = Part.objects.filter(out_of_stock=True, inactive=False).order_by('part_no')
        elif inactive:
                parts = Part.objects.filter(inactive=True).order_by('part_no')
        else:
            parts = Part.objects.all().order_by('part_no')
    paginator = Paginator(parts, 25) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list-parts.html', {'page_obj': page_obj})
    
@login_required(login_url='/login')
def addPart(request):
    form = PartForm()
    if request.method == 'POST':
        part_form = PartForm(request.POST)
        if part_form.is_valid():
            bikes = request.POST.getlist('bikes')
            bikes_list = bikes if bikes else ['n/a']
            part = part_form.save(commit=False)
            part.bike_models = bikes_list
            part.save()
            msg = 'part added'
            return render(request, 'add-part.html', {'form':form, 'msg': msg})
        else:
            print(part_form.errors)
    return render(request, 'add-part.html', {'form':form})


@login_required(login_url='/login')
def editPart(request, id):
    part = get_object_or_404(Part, id=id)
    form = PartForm(instance=part)
    delete = request.POST.get('delete')
    if delete:
        part.delete()
        return redirect('parts:list-parts')
    if request.POST:
        bikes = request.POST.getlist('bikes')
        bikes_list = bikes if bikes else ['n/a']
        part_form = PartForm(request.POST, instance=part)
        part_form.save(commit=False)
        part.bike_models = bikes_list
        part.save()
        return redirect('parts:list-parts')
    return render(request, 'edit-part.html', {'form': form})


@login_required(login_url='/login')
def excels(request):
    excels = ExcelSheet.objects.only('upload_date')
    return render(request, 'excels.html', {'excels':excels})

@login_required(login_url='/login')
def excelDetail(request, id):
    excel = get_object_or_404(ExcelSheet, id=id)
    return render(request, 'excel-detail.html', {'excel': excel})


def ajax_view(request):
    search = request.GET.get('search')
    language = request.GET.get('language')
    try:
        int(search)
        parts = Part.objects.values().filter(part_no=search)
    except:
        if language == 'danish':
            parts = Part.objects.values().filter(danish_slug__contains=search).order_by('title')
        else:
            parts = Part.objects.values().filter(slug__contains=search).order_by('slug')
    res = []
    for i in parts:
        res.append(i)
    return JsonResponse(res, safe=False)


def upload(request):
    parts = Part.objects.filter(out_of_stock=True)
    for part in parts:
        print(part.title)
    

   
    return render(request, 'upload.html')








