from rest_framework import viewsets,permissions
from .serializers import patient_registrationSerializer
from .models import patient_registration

class patient_registrationViewSet(viewsets.ModelViewSet):
    queryset = patient_registration.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_registrationSerializer