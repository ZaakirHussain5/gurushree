from django.urls import path, include
from rest_framework import routers
from . import views


from .api import (patient_registrationViewSet,billheaderViewSet,billdetailsViewSet,billreceiptViewSet, pendingBalanceView, appointmentView,
        PrescriptionMedicationViewSet, PrescriptionHeaderViewSet
)

router = routers.DefaultRouter()
router.register('patient_registration',patient_registrationViewSet,'patient_registration')
router.register('billheader',billheaderViewSet,'billheader')
router.register('billdetails',billdetailsViewSet,'billdetails')
router.register('billreceipt',billreceiptViewSet,'billreceipt')
router.register('pendingBalanceView',pendingBalanceView,'pendingBalanceView')
router.register('appointmentView', appointmentView, 'appointmentView')
router.register('prescription', PrescriptionHeaderViewSet, 'prescription')
router.register('medication', PrescriptionMedicationViewSet, 'medication')

urlpatterns=[
    path('', include(router.urls)), 
    path('getConsultationSlots', views.getConsultationSlots, name='slots'),

]