from unicodedata import category
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('blog/<int:id>/',views.post,name='detail'),
    path('category/<str:title>/',views.category,name='all_category'),

]
