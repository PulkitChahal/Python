from django.contrib import admin
from .models import Employees, Manager, Employee


# Register your models here.
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'empid', 'ename', 'eaddress', 'email']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'mail', 'age']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'mail', 'age']

# admin.site.register(Employees)
