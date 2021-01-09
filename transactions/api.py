from rest_framework import viewsets,permissions
from .serializers import (patient_registrationSerializer,billheaderSerializer,billdetailsSerializer,billreceiptSerializer,
        BookAppointmentsSerializer, PrescriptionMedicationSerializer, PrescriptionHeaderSerializer 
)
from .models import ( patient_registration,billheader,billdetails,billreceipt, BookAppointments, PrescriptionMedication, 
        PrescriptionHeader 
)
from django.db.models import F


class patient_registrationViewSet(viewsets.ModelViewSet):
    queryset = patient_registration.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_registrationSerializer


class billheaderViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = billheaderSerializer

    def get_queryset(self):
        queryset = billheader.objects.all()
        bill_id = self.request.query_params.get('id', None)
        if bill_id:
            queryset = billheader.objects.filter(id=bill_id) 
            print(queryset)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.first_name + self.request.user.last_name
        bill_header = serializer.save(AddedBy =user, EditedBy=user)
        patient_data = patient_registration.objects.get(id=self.request.data['patient'])
        bill_header.patient = patient_data
        bill_header.save()
        return bill_header

    # def perform_update(self, serializer):
    #     id = self.request.data['id']
    #     billheader.objects.get(id=id)

class billdetailsViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billdetailsSerializer


    def get_queryset(self):
        queryset = billdetails.objects.all()
        bill_code = self.request.query_params.get('bill_code', None)
        if bill_code:
            queryset = billdetails.objects.filter(BillCode=bill_code)
        return queryset


class billreceiptViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billreceiptSerializer

    def get_queryset(self):
        queryset = billreceipt.objects.all()    
        bill_code = self.request.query_params.get('BillCode', None)
        if bill_code:
            queryset = billreceipt.objects.filter(BillCode=bill_code)
        
        return queryset




    def perform_create(self, serializer):
        user = self.request.user.first_name + self.request.user.last_name
        bill_recept = serializer.save(AddedBy=user, EditedBy=user)
        if bill_recept.RecMode == 'Balance':
            bill_header = billheader.objects.get(id = bill_recept.BillCode)
            bill_header.Balance = self.request.data['availableBalance']
            bill_header.PaidAmount = bill_header.TotalAmount - bill_header.Balance
            bill_header.save()
        return bill_recept

class pendingBalanceView(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billheaderSerializer

    def get_queryset(self):
        queryset = billheader.objects.filter(TotalAmount__gt = F('PaidAmount'))
        return queryset


class appointmentView(viewsets.ModelViewSet):
    queryset = BookAppointments.objects.all()
    serializer_class = BookAppointmentsSerializer
    permissions = [
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        user = self.request.user.first_name + self.request.user.last_name
        serializer.save(AddedBy=user, EditedBy=user)


class PrescriptionHeaderViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionHeader.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = PrescriptionHeaderSerializer

    
class PrescriptionMedicationViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionMedication.objects.all()
    permissions = [
        permissions.AllowAny
    ]

    serializer_class = PrescriptionMedicationSerializer


