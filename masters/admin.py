from django.contrib import admin
from .models import professional, ConsultantSlotMaster, Department, hospital, discounType, service, registrationType, generalType
# Register your models here.
# admin.site.site_header = 'Gurushree Admin Panel' 
admin.empty_value_display = '**Empty**'
admin.site.register((ConsultantSlotMaster, Department,registrationType, hospital, discounType, service, generalType))
# admin.site.register()



# class professionalAdmin(admin.ModelAdmin): 
#     list_display = ('id', 'professionalName', 'department', 'category', 'contactNo', 'email')
    
#     # def has_add_permission(self, request): 
#     #     return False
    
#     # def has_delete_permission(self, request): 
#     #     return False

#     def has_search_permission(self, request):
#         return True

        
#     fieldsets = [
#         ['Required fields are here', {
#             'fields': [ 'professionalName', 'department', 'category', 'contactNo', 'email']
#         }],
#         ['Optional field are here', {
#             'fields': ['title', 'qualification', 'designation', 'OPNewVisit', 'OPRevisit', 'OPfollowup', 'OPShare', 'OPShareamount',
#                 'IPAmount', 'IPShare', 'IPShareamount', 'licenceNo', 'photo', 'hospitalName', 'priority', 
#                 'token', 'appointment', 'duration', 'isActive', 'addedBY', 'editedby'
#                 ],
#         }],
#     ]
#     search_fields = ('professionalName__istartswith', 'designation', 'email', 'contactNo')


admin.site.register(professional)