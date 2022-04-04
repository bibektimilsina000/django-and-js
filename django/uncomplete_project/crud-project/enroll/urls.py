
from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.add_show,name='add_show_user'),
    path('delete/<int:id>/',views.deletedata,name='deletedata'),
    path('<int:id>/',views.update_data,name='update_data'),
]
