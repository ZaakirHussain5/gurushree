from rest_framework import serializers
from .models import GenType, State, City, Area, Department, SubDepartment,packagemapping, generalType, registrationType, discounType, user, income_expenses, hospital, professional, menu, pagemaster,service


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
