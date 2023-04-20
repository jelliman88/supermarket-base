from django.urls import path

from . import views


app_name = 'parts'
urlpatterns = [
     path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('accounts', views.accounts, name='accounts'),
    path('add-account', views.add_account, name='add-account'),
    path('account-detail/<int:id>', views.account_detail, name='account-detail'),
    path('list-parts', views.listParts, name='list-parts'),
    path('edit-part/<int:id>', views.editPart, name='edit-part'),
    path('add-part', views.addPart, name='add-part'),
    path('excels', views.excels, name='excels'),
    path('excel-detail/<int:id>', views.excelDetail, name='excel-detail'),
    path('ajax/', views.ajax_view, name="ajax"),
    path('upload/', views.upload, name="upload"),

]