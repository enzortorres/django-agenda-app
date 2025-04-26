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
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'), # delete
]
