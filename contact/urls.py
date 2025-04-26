from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # home
    path('', views.index, name='index'),
    
    # search
    path('search/', views.search, name='search'),
    
    # contact (CRUD)
    path('contact/create/', views.create, name='create'), # create
    path('contact/<int:contact_id>/', views.contact, name='contact'), # read
    path('contact/<int:contact_id>/update/', views.update, name='update'), # update
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # delete
    
    # user
    path('user/register/', views.register, name='register'), # register 
    path('user/login/', views.login_view, name='login'), # login 
    path('user/logout/', views.logout_view, name='logout'), # logout 
    
]
