from django.shortcuts import render
from testapp.models import Student
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import HttpsResponseMixin, SerializeMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(HttpsResponseMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            s = Student.objects.get(id=id)
        except Student.DoesNotExist:
            s = None
        return s

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps(
                {'msg': 'Please Provide Valid JSON Data Only'}), status=400)

        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            student = self.get_object_by_id(id)
            if student is None:
                return self.render_to_http_response(json.dumps(
                    {'msg': 'No Matched Record Found With Matched ID'}), status=404)

            json_data = self.serialize_to_json([student, ])
            return self.render_to_http_response(json_data)

        qs = Student.objects.all()
        json_data = self.serialize_to_json(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps(
                {'msg': 'Please Provide Valid JSON Data Only'}), status=400)

        std_data = json.loads(data)
        form = StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps(
                {'msg': 'Student Data Created Successfully'}))

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps(
                {'msg': 'Please Provide Valid JSON Data Only'}), status=400)

        provided_data = json.loads(data)
        id = provided_data.get('id', None)
        if id is None:
            return self.render_to_http_response(json.dumps({
                'msg': 'No ID Provided To Update Data'}), status=400)

        student = self.get_object_by_id(id)
        if student is None:
            return self.render_to_http_response(json.dumps(
                {'msg': 'No Matched Record Found With Given ID'}), status=404)

        original_data = {
            'name': student.name,
            'rollno': student.rollno,
            'marks': student.marks,
            'gf': student.gf,
            'bf': student.bf,
        }
        original_data.update(provided_data)
        form = StudentForm(original_data, instance=student)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps(
                {'msg': 'Student Data Updated Successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps(
                {'msg': 'Please Provide Valid JSON Data Only'}), status=400)

        provided_data = json.loads(data)
        id = provided_data.get('id', None)
        if id is None:
            return self.render_to_http_response(json.dumps({
                'msg': 'No ID Provided To Delete Data'}), status=400)

        student = self.get_object_by_id(id)
        if student is None:
            return self.render_to_http_response(json.dumps(
                {'msg': 'No Matched Record Found With Given ID To Delete'}), status=404)

        status, deleted_item = student.delete()
        if status == 1:
            return self.render_to_http_response(json.dumps(
                {'msg': 'Student Data Deleted Successfully'}))

        json_data = json.dumps({'msg': 'Unable to Delete Data Please Try Again'})
        return self.render_to_http_response(json_data, status=500)
