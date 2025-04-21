from rest_framework import serializers
from .models import *


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employees
#         fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    age = models.IntegerField()

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

    class Meta:
        model = Manager
        fields = '__all__'


def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError("Name must start with 'S'.")


class EmployeeSerializer(serializers.ModelSerializer):
    name = models.CharField(max_length=20, validators=[start_with_s])
    address = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    age = models.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Employee must be at least 18 years old.")
        elif value > 100:
            raise serializers.ValidationError("Employee's age cannot be greater than 100.")
        return value

    class Meta:
        model = Employee
        fields = '__all__'
