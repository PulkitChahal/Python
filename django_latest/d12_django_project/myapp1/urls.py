from django.urls import path
from . import views

urlpatterns = [
    path('v3/', views.v3, name='v3'),
    path('v4/', views.v4, name='v4'),
]