from rest_framework import routers
from .api import patient_registrationViewSet

router = routers.DefaultRouter()
router.register('patient_registration',patient_registrationViewSet,'patient_registration')

urlpatterns=router.urls