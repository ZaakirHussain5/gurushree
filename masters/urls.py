from rest_framework import routers
from .api import ( GenTypeViewSet, SubdepartmentsListViewSet,packagemappingViewSet, serviceViewSet, 
        DepartmentViewSet, CitiesListViewSet, StateViewSet, CityViewSet,
        AreaViewSet, SubDepartmentViewSet, GeneralTypeViewSet, registrationTypeViewSet, 
        discounTypeViewSet, userViewSet, income_expensesViewSet, hospitalViewSet, 
        professionalViewSet, menuViewSet, pagemasterViewSet, ConsultantSlutMasterViewSet,
        slotsLists, check_discount

)
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet, 'departments')
router.register('subdepartments', SubDepartmentViewSet, 'subdepartments')
router.register('generalTypes', GeneralTypeViewSet, 'generalTypes')
router.register('registrationType', registrationTypeViewSet, 'registrationType')
router.register('user', userViewSet, 'user')
router.register('income_expenses', income_expensesViewSet, 'income_expenses')
router.register('hospital', hospitalViewSet, 'hospital')
router.register('professional', professionalViewSet, 'professional')
router.register('menu', menuViewSet, 'menu')
router.register('pagemaster', pagemasterViewSet, 'pagemaster')
router.register('states', StateViewSet, 'states')
router.register('cities', CityViewSet, 'cities')
router.register('areas', AreaViewSet, 'areas')
router.register('citieslist', CitiesListViewSet, 'citieslist')
router.register('subdepartmentsList', SubdepartmentsListViewSet, 'subdepartmentsList')
router.register('gentypes', GenTypeViewSet, 'gentypes')
router.register('discountypes', discounTypeViewSet, 'discountypes')
# router.register('checkDiscountType', views.verify_discount, 'check_discount')
router.register('service', serviceViewSet, 'service')
router.register('packagemapping', packagemappingViewSet, 'packagemapping')

router.register('ConsultantSlutMaster', ConsultantSlutMasterViewSet, 'ConsultantSlutMasterViewSet')
router.register('availabilitySlots', slotsLists, 'slotsLists')




# urlpatterns = router.urls
urlpatterns = [
        path('', include(router.urls)), 
        path('checkDiscountType/', views.verify_discount, name="check_discount")
        ]


