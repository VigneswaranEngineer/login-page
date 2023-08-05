from django.urls import path
from . import views

#url config
urlpatterns = [
    path('hello/',views.say_hello,name="hello"),
    path('hello/add',views.arithmetic,name='add')
    
    
]