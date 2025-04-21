from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Employees
from .serializers import *
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views import View
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class EmployeeModelView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]


class CustomerViewset(viewsets.ViewSet):
    def list(self, request):
        print(f'Basename: {self.basename}')
        print(f'Action: {self.action}')
        print(f'Detail: {self.detail}')
        print(f'Name: {self.name}')
        emp = Employees.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)


class RetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetails(APIView):
    def get(self, request):
        emp = Employees.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def emp_details(request, pk):
    emp = Employees.objects.get(id=pk)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def emp_all_details(request):
    emp = Employees.objects.all()
    serializer = EmployeeSerializer(emp, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def create_manager(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = ManagerSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            result = {'message': 'Data Inserted Into Database'}
            json_data = JSONRenderer().render(result)
            return HttpResponse(json_data, content_type='application/json')

    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json', status=400)


def get_data(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
            manager = Manager.objects.get(id=id)
            serializer = ManagerSerializer(manager)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeData(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            data = request.body
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id', None)
            if id is not None:
                emp = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(emp)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')

            emps = Employee.objects.all()
            serializer = EmployeeSerializer(emps, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.body
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            serializer = EmployeeSerializer(data=py_data)
            if serializer.is_valid():
                serializer.save()
                result = {'message': 'Data Inserted Into Database'}
                json_data = JSONRenderer().render(result)
                return HttpResponse(json_data, content_type='application/json')

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            data = request.body
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id', None)
            if id is not None:
                emp = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(emp, data=py_data)
                if serializer.is_valid():
                    serializer.save()
                    result = {'message': 'Data Updated Successfully'}
                    json_data = JSONRenderer().render(result)
                    return HttpResponse(json_data, content_type='application/json')

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            data = request.body
            stream = io.BytesIO(data)
            py_data = JSONParser().parse(stream)
            id = py_data.get('id', None)
            if id is not None:
                emp = Employee.objects.get(id=id)
                emp.delete()
                result = {'message': 'Data Deleted Successfully'}
                json_data = JSONRenderer().render(result)
                return HttpResponse(json_data, content_type='application/json')

            json_data = JSONRenderer().render({'error': 'No Id Provided'})
            return HttpResponse(json_data, content_type='application/json', status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return Response(serializer.data)


class EmployeeAPIView(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return Response(serializer.data)


class ListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
