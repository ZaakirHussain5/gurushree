from .serializers import GenTypeSerializer, SubDepartmentsListSerializer,packagemappingSerializer, DepartmentSerializer,packagemappingSerializer, CitiesListSerializer, SubDepartmentSerializer, GeneralTypeSerializer, registrationTypeSerializer, discounTypeSerializer, userSerializer, income_expensesSerializer, hospitalSerializer, professionalSerializer, menuSerializer, pagemasterSerializer, StateSerializer, AreaSerializer, CitySerializer,serviceSerializer
from .models import GenType, Department, SubDepartment, generalType,packagemapping, registrationType,packagemapping, discounType, user, income_expenses, hospital, professional, menu, pagemaster, State, City, Area,service
from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.hashers import make_password

class DepartmentViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.all()
        flag = self.request.query_params.get('isActive', None)
        if flag is not None:
            queryset = queryset.filter(isActive=flag)
        return queryset


class SubDepartmentViewSet(viewsets.ModelViewSet):
    queryset = SubDepartment.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SubDepartmentSerializer


class GeneralTypeViewSet(viewsets.ModelViewSet):
    #queryset = generalType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = GeneralTypeSerializer

    def get_queryset(self):
        queryset = generalType.objects.all()
        gentype = self.request.query_params.get('gentype', None)
        if gentype is not None:
            queryset = queryset.filter(genType=gentype).filter(isActive=True)
        return queryset


class registrationTypeViewSet(viewsets.ModelViewSet):
    queryset = registrationType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = registrationTypeSerializer


class discounTypeViewSet(viewsets.ModelViewSet):
    queryset = discounType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = discounTypeSerializer

    def perform_create(self, serializer):
        import random
        n = random.randint(1000,9999)
        plainPass=str(n)
        password = make_password(plainPass)
        serializer.save(password=password)

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class userViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer
    def get_queryset(self):
        queryset = user.objects.all()
        flag = self.request.query_params.get('isactive', None)
        if flag is not None:
            queryset = queryset.filter(isactive=flag)
        return queryset


class income_expensesViewSet(viewsets.ModelViewSet):
    queryset = income_expenses.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = income_expensesSerializer


class hospitalViewSet(viewsets.ModelViewSet):
    queryset = hospital.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = hospitalSerializer


class professionalViewSet(viewsets.ModelViewSet):
    queryset = professional.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = professionalSerializer


class menuViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = menuSerializer
    def get_queryset(self):
        queryset = menu.objects.all()
        flag = self.request.query_params.get('isActive', None)
        if flag is not None:
            queryset = queryset.filter(isActive=flag)
        return queryset



class pagemasterViewSet(viewsets.ModelViewSet):
    queryset = pagemaster.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = pagemasterSerializer


class StateViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = StateSerializer

    def get_queryset(self):
        queryset = State.objects.all()
        flag = self.request.query_params.get('isActive', None)
        if flag is not None:
            queryset = queryset.filter(isActive=flag)
        return queryset


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = AreaSerializer


class CitiesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CitiesListSerializer
    def get_queryset(self):
            queryset = City.objects.all()
            flag = self.request.query_params.get('isActive', None)
            if flag is not None:
                queryset = queryset.filter(isActive=flag)
            return queryset
    

class SubdepartmentsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SubDepartmentsListSerializer
   
    def get_queryset(self):
        queryset = SubDepartment.objects.all()
        flag = self.request.query_params.get('isActive', None)
        if flag is not None:
            queryset = queryset.filter(isActive=flag)
        return queryset
    

class GenTypeViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class =GenTypeSerializer

    def get_queryset(self):
        queryset = GenType.objects.all()
        flag = self.request.query_params.get('isActive', None)
        if flag is not None:
            queryset = queryset.filter(isActive=flag)
        return queryset

class serviceViewSet(viewsets.ModelViewSet):
    queryset = service.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = serviceSerializer

packagemappingSerializer


class packagemappingViewSet(viewsets.ModelViewSet):
    queryset = packagemapping.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = packagemappingSerializer