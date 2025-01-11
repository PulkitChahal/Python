from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    resp = f'<h1>Employee Number: {emp_data["eno"]}<br> Employee Name: {emp_data["ename"]}<br> Employee Salary: {emp_data["esal"]}<br> Employee Address: {emp_data["eaddr"]}</h1>'

    return HttpResponse(resp)


def emp_data_json_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')


def emp_data_json_view_2(request):
    emp_data = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Mumbai',
    }
    return JsonResponse(emp_data)


from django.views.generic import View


class JsonCBV(View):
    # def get(self, request, *args, **kwargs):
    #     emp_data = {
    #         'eno': 100,
    #         'ename': 'Sunny',
    #         'esal': 1000,
    #         'eaddr': 'Mumbai',
    #     }
    #     return JsonResponse(emp_data)

    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from post method'})
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from put method'})
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from delete method'})
        return HttpResponse(json_data, content_type='application/json')


from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize


class EmployeeDetailCBV(View):
    def get(self, request, id, *args, **kwargs):
        # emp = Employee.objects.get(id=1)
        # emp = Employee.objects.get(id=id)
        # emp_data = {
        #     'eno': emp.eno,
        #     'ename': emp.ename,
        #     'esal': emp.esal,
        #     'eaddr': emp.eaddr,
        # }
        # json_data = json.dumps(emp_data)

        emp = Employee.objects.get(id=id)
        # json_data = json.dumps({'msg': 'The requested resource not available'})
        json_data = serialize('json', emp, fields=('eno', 'ename', 'esal', 'eaddr'))
        return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV(View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        json_data = serialize('json', emp, fields=('eno', 'ename', 'eaddr'))
        pdict = json.loads(json_data)
        final_list = []
        for obj in pdict:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')


from testapp.mixin import SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV2(SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        json_data = self.serialize(emp)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send Valid json data only'})
            return HttpResponse(json_data, content_type='application/json', status=400)

        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Employee created successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Employee not found'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send Valid json data only'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Employee Data Updated successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'Employee not found'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Employee deleted successfully'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        json_data = json.dumps({'msg': 'Unable to delete Employee data'})
        return HttpResponse(json_data, content_type='application/json', status=200)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpResponse, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send Valid json data only'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'Employee not found'})
                return HttpResponse(json_data, content_type='application/json', status=404)
            json_data = self.serialize(emp)
            return HttpResponse(json_data, content_type='application/json', status=200)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json', status=200)
