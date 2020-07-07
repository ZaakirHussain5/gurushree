from rest_framework import serializers
from .models import patient_registration

class patient_registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=patient_registration
        fields='__all__'