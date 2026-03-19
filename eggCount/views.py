from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages


def main (request):
    chickrooms = rooms.objects.all()
    template = loader.get_template('egg_collection.html')

    if request.method == 'POST':
        room_id = request.POST['room_no']
        room_obj = get_object_or_404(rooms, id=room_id)
        if room_obj.room_status == 'active':
            room_record = eggHatch(
            room = room_obj,
            eggsNo = request.POST['egg_no'],
            period = request.POST['period']
            )
            room_record.save()
            return redirect('records')
        else:
            messages.error(request, "please activate room first")

        

    context = {
        'chickrooms' : chickrooms,
    }
    
    return HttpResponse(template.render(context, request))


def room_register(request):
    template = loader.get_template('room_registration.html')
    chickrooms = rooms.objects.all()
    if request.method == 'POST':
        room_record = rooms(
            roomNo = request.POST['room_no'],
            ChickensNo = request.POST['capacity'],
            room_status = request.POST['type']
        )

        room_record.save()

    return HttpResponse(template.render())

def view_records(request):
    chickrooms = rooms.objects.all()
    template = loader.get_template('view_records.html')

    context = {
        'chickrooms' : chickrooms,
    }
    return HttpResponse(template.render(context, request))

def room_details(request, id):
    chickroom = get_object_or_404(rooms, id=id)
    room_data = chickroom.hatches.all()
    template = loader.get_template('room_details.html')

    if request.method == 'POST':
        if chickroom.room_status == 'active':
            chickroom.room_status = 'inactive'
        else:
            chickroom.room_status= 'active'

        chickroom.save()
        return redirect('records')


    context = {
        'chickroom' : chickroom,
        'room_data' : room_data,
    }

    return HttpResponse(template.render(context, request))

def pdf_format(request, id):
    chickroom = get_object_or_404(rooms, id=id)
    room_data = chickroom.hatches.all()
    template = loader.get_template('record_per_room_pdf.html')

    context = {
        'chickroom' : chickroom,
        'room_data' : room_data
    }
    return HttpResponse(template.render(context, request))