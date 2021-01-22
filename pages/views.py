from django.shortcuts import render,redirect
from transactions.models import patient_registration, billdetails, billheader, billreceipt, PrescriptionHeader, PrescriptionMedication
from masters.models import professional, Department
from django.db.models import F
from masters.models import hospital, registrationType, generalType

def index(request):
    return render(request, 'auth/index.html')


def login(request):
    context = {}
    try:
        context['hospital'] = hospital.objects.first()
    except hospital.DoesNotExist:
        pass
    return render(request, 'auth/login.html', context)


def dashboard(request):
    return render(request, 'auth/dashboard.html')


def departments(request):
    return render(request, 'masters/departments.html')


def places(request):
    return render(request, 'masters/places.html')


def regTypes(request):
    return render(request, 'masters/regTypes.html')


def disctype(request):
    return render(request, 'masters/disTypes.html')

    
def generals(request):
    return render(request, 'masters/generals.html')


def incomeExpenses(request):
    return render(request, 'masters/incomeExpenses.html')


def menus(request):
    return render(request, 'masters/menus.html')


def pages(request):
    return render(request, 'masters/pages.html')


def hospitals(request):
    return render(request, 'masters/hospitals.html')


def users(request):
    return render(request, 'masters/users.html')


def professionals(request):
    return render(request, 'masters/professionals.html')

def genTypes(request):
    return render(request,'masters/genTypes.html')


def disType(request):
    return render(request,'masters/disTypes.html')

def services(request):
    return render(request,'masters/services.html')

def packagemap(request):
    return render(request,'masters/packagemap.html')

def patientReg(request):
    context = {}
    
    active_types = generalType.objects.filter(isActive=True)
    context['registration_type'] = registrationType.objects.all()
    context['titles'] = active_types.filter(genType='Title')
    context['marital_status'] = active_types.filter(genType='Marital Status')
    context['religions'] = active_types.filter(genType='Religion')
    context['blood_groups'] =active_types.filter(genType='Blood Group')
    context['nationalitys'] = active_types.filter(genType='Nationality')
    context['RelationTypes'] = active_types.filter(genType='Relation Type')
    context['identifications'] = active_types.filter(genType='Identification')
    context['occupations'] = active_types.filter(genType='Occupation')
    return render(request,'transactions/patientReg.html', context)

def op_billing(request):
    if request.GET.get('patient_id'):
        patient = patient_registration.objects.get(id=request.GET.get('patient_id'))
        consultants = professional.objects.filter(category='C')
        Refferals = professional.objects.filter(category='R')
        return render(request,'transactions/op_billing.html',{
            "patient":patient,
            "consultants":consultants,
            "refferals":Refferals
        })
    else:
        return redirect('/trans/patientReg')


def invoice(request):
    bilhead_id = request.GET.get('bilhead_id', None)
    if bilhead_id is not None:
        context = {}
        bill_payment_details = {
            'bill_total': 0,
            'bill_cash': 0,
            'bill_card':0,
            'bill_other': 0
        }
        bill_header = billheader.objects.get(id = bilhead_id)
        context['bill_header'] = bill_header
        service = billdetails.objects.filter(BillCode = bill_header.id)
        bill_receipts = billreceipt.objects.filter(BillCode = bill_header.id).order_by('-id')
        context['services'] = service
        context['receipts'] = bill_receipts
        for bill in bill_receipts:
            bill_payment_details['bill_total'] = ( bill.RecAmount + bill_payment_details['bill_total'])
            bill_payment_details['bill_cash'] = ( bill.Cash + bill_payment_details['bill_cash'])
            bill_payment_details['bill_card'] = ( bill.CardTotal + bill_payment_details['bill_card'])
            bill_payment_details['bill_other'] = ( bill.OtherPaid + bill_payment_details['bill_other'])
        context['bill_details'] = bill_payment_details
        context['hospital'] = hospital.objects.first()
        return render(request, 'transactions/print_bill.html', context)
        # except:
        #     pass


def pendingBalanceList(request):
    return render(request, 'transactions/pedingBalanceList.html')

def billLists(request):
    return render(request, 'transactions/bill_lists.html')

def edit_bill(request, id):
    
    return render(request, 'transactions/editBill.html', {"id": id})


def appointments(request):
    patient_id = request.GET.get('patient_id', None)
    context = {}

    if patient_id:
        try:
            patient = patient_registration.objects.get(id=patient_id)
            context['patient'] = patient
        except:
            return redirect('index')
    else:
        return redirect('/')
    departments = Department.objects.all()
    context['departmetns'] = departments
    return render(request, 'transactions/newAppointments.html', context)


def slots(request):
    return render(request, 'masters/slots.html')


def prescriptions(request):
    pat_id = request.GET.get('patient_id', None)
    context = {}
    if pat_id:
        pat_reg = patient_registration.objects.get(id=pat_id)
        bills = billheader.objects.filter(patient = pat_reg)
        bill_details = billdetails.objects.filter(BillCode__in=[b.id for b in bills ]).exclude(DrCode=None)
        context['bills'] = bill_details

    return render(request, 'transactions/prescriptions.html', context)



def invoice_prescription(request):
    context = {}
    prescription_id = request.GET.get('id')
    prescription = PrescriptionHeader.objects.get(id=prescription_id)
    medications = prescription.medications.all()
    context['medications'] = medications
    context['prescription'] = prescription
    print(medications)
    print(prescription)
    return render(request, 'transactions/prescription_print.html', context)

























