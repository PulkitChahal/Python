from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.v1, name='1'),
    path('v2/', views.v2, name='v2'),
    path('t/', views.date_time, name='date_time'),
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('index/', views.index, name='index'),
    path('emp/', views.emp_details, name='emp_details'),
    path('v3/', views.v3, name='v3'),
    path('form/', views.student, name='student'),
]