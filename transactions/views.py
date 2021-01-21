from django.shortcuts import render
from django.http import JsonResponse
from masters.models import professional, ConsultantSlotMaster
import datetime
import json
# Create your views here.

def getConsultationSlots(request):

    professional_id = request.GET.get('id')
    date = request.GET.get('date')
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    day_name = date_obj.strftime("%A")
    try:
        professionals = professional.objects.get(id=professional_id)
    except:
        queryset = []
        return JsonResponse({"data": []})

    queryset = ConsultantSlotMaster.objects.filter(consultant_id=professionals, day__icontains=day_name)
    data = []
    for consultant in queryset:
        obj = {}
        obj['day'] = consultant.get_dayName
        current_datetime = datetime.datetime.now()
        str_make_date = str(current_datetime.year) + '-' + str(current_datetime.month) + '-' + str(current_datetime.day) + ' '+ consultant.time_from
        str_make_date_to = str(current_datetime.year) + '-' + str(current_datetime.month) + '-' + str(current_datetime.day) + ' '+ consultant.time_to
        from_time = datetime.datetime.strptime(str_make_date, "%Y-%m-%d %H:%M")
        to_time = datetime.datetime.strptime(str_make_date_to, "%Y-%m-%d %H:%M")
        slot_number = consultant.slot_duration
        slots = []
        while from_time < to_time:
            from_time = from_time + datetime.timedelta( minutes= slot_number )
            if(from_time < to_time):
                str_time = from_time.strftime("%I:%M " '%p')
                slots.append(str_time)
        obj['slots'] = slots
        data.append(obj)

    return JsonResponse({"data": json.dumps(data)})
