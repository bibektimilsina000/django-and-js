
from django.urls import path
from apps_c import views


urlpatterns = [
    
    path('', views.SignUpView.as_view(),name='home'),
]
