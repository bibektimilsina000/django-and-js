from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.emp_form,name='home'),
    path('list',views.emp_list,name='list'),
]


