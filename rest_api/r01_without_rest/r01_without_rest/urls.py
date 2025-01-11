"""
URL configuration for r01_without_rest project.

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
from django.urls import path, re_path
from testapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', views.emp_data_view),
    path('apijson/', views.emp_data_json_view),
    path('apijson2/', views.emp_data_json_view_2),
    path('apijsoncbv', views.JsonCBV.as_view()),
    # path('api2/', views.EmployeeDetailCBV.as_view()),
    re_path(r'^api2/(?P<id>\d+)/$', views.EmployeeDetailCBV.as_view()),
    path(r'api3/', views.EmployeeListCBV2.as_view()),
    path(r'api_data/', views.EmployeeCRUDCBV.as_view()),
]
