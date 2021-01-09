from rest_framework import serializers
from .models import (patient_registration,billheader,billdetails,billreceipt, BookAppointments, PrescriptionHeader,
        PrescriptionMedication
)

class patient_registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=patient_registration
        fields='__all__'

class billheaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=billheader
        fields='__all__'
        depth = 1
class billdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=billdetails
        fields='__all__'

class billreceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=billreceipt
        fields='__all__'


class BookAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAppointments
        fields='__all__'


class PrescriptionHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionHeader
        fields = '__all__'


class PrescriptionMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedication
        fields = '__all__'


        