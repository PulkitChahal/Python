from django.contrib import admin
from testApp.models import Employee, Student


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student)
