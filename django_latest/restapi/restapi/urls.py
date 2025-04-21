"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from RestApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('EmployeeModelView', views.EmployeeModelView, basename='manager')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('emp/', views.EmployeeDetails.as_view()),
    # path('emp/<int:pk>', views.emp_details),
    # path('empall/', views.emp_all_details),
    # path('createmanager/', views.create_manager),
    # path('getdata/', views.get_data),
    # path('emp/', views.EmployeeAPIView.as_view()),
    # path('LC/', views.ListCreate.as_view()),
    # path('RUD/<int:pk>', views.RetrieveUpdateDelete.as_view()),
    path('', include(router.urls))

]
