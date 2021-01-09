from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .passwordHandle import PasswordHandle
import hashlib, os, binascii

from .models import (GenType, State, City, Area, Department, SubDepartment, 
        packagemapping, generalType, registrationType, discounType, user, 
        income_expenses, hospital, professional, menu, pagemaster, service,
        ConsultantSlutMaster
)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = '__all__'


class GeneralTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = generalType
        fields = '__all__'


class registrationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrationType
        fields = '__all__'


class discounTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = discounType
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        print(password)
        my_pass_handlr = PasswordHandle()
        hash_password = my_pass_handlr.hash_password(password)
        discount = discounType(
            discType=validated_data.get('discType', None),
            discount = validated_data.get('discount', None),
            userId = validated_data.get('userId'),
            password = hash_password,
            isActive=validated_data.get('isActive', None)
        )
        discount.save()
        return discount


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class income_expensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = income_expenses
        fields = '__all__'


class hospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospital
        fields = '__all__'


class professionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = professional
        fields = '__all__'


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'


class pagemasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagemaster
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class CitiesListSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = '__all__'

class SubDepartmentsListSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer()

    class Meta:
        model=SubDepartment
        fields='__all__'

class GenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GenType
        fields='__all__'

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=service
        fields='__all__'

        
class packagemappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=packagemapping
        fields='__all__'


class ConsultantSlutMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantSlutMaster
        fields = [
                'id',
                'consultant_id',
                'get_name',
                'day', 
                'time_from', 
                'time_to', 
                'slot_duration'
            ]