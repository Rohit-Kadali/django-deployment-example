
from django.urls import path 
from My_app import views

app_name = 'My_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]