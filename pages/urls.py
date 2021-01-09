from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='register'),
    path('masters/departments', views.departments, name='departments'),
    path('masters/Places', views.places, name='places'),
    path('masters/Generals', views.generals, name='generals'),
    path('masters/GenTypes', views.genTypes, name='genTypes'),
    path('masters/distypes', views.disType, name='disTypes'),
    path('masters/RegTypes', views.regTypes, name='regtypes'),
    path('masters/Pages', views.pages, name='pages'),
    path('masters/menus', views.menus, name='menus'),
    path('masters/incomeExpenses', views.incomeExpenses, name='incomeExpenses'),
    path('masters/hospitals', views.hospitals, name='hospitals'),
    path('masters/users', views.users, name='users'),
    path('masters/professionals', views.professionals, name='professionals'),
    path('masters/services', views.services, name='services'),
    path('masters/packagemaping', views.packagemap, name='packagemaping'),
    path('masters/slots', views.slots, name='slots' ),
    path('masters/discType', views.disctype, name="disctype"),

    path('trans/patientReg', views.patientReg, name='patientReg'),
    path('trans/op_billing', views.op_billing, name='op_billing'),
    path('trans/invoice', views.invoice, name="invoice"),
    path('trans/pendingBalances', views.pendingBalanceList, name="pendingBalanceList"),
    path('trans/BillLists/', views.billLists, name="bill_list"),
    path('trans/editBill/<id>/', views.edit_bill, name="edit_bill"),
    path('trans/appointments', views.appointments, name="new_appointment"),
    path('trans/prescription', views.prescriptions, name='new_prescription'),
    path('trans/prescription/invoice', views.invoice_prescription, name='print_invoice'),

    
    
]
