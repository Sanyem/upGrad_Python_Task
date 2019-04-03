from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
import datetime

@login_required(login_url='/')
def dashboard(request):
    upcoming_schedule_list = schedule.objects.filter(user__username=request.user.username, date__gte=datetime.datetime.today())
    previous_schedule_list = schedule.objects.filter(user__username=request.user.username, date__lte=datetime.datetime.today())
    return render(request, 'schedule/schedule.html', {'upcoming_schedule_list':upcoming_schedule_list, 'previous_schedule_list':previous_schedule_list})

@login_required(login_url='/')
def addSchedule(request):
    if request.method == 'GET':
        return render(request, 'schedule/add-schedule.html')

    if request.method == 'POST':
        obj_schedule = schedule()
        obj_schedule.user = request.user
        obj_schedule.topic = request.POST.get('schedule_topic')
        obj_schedule.date = request.POST.get('schedule_date')
        obj_schedule.start_time = request.POST.get('schedule_start_time')
        obj_schedule.end_time = request.POST.get('schedule_end_time')
        obj_schedule.save()

        messages.success(request, 'SCHEDULE CREATED SUCCESSFULLY')
        return HttpResponseRedirect(reverse('schedule:dashboard'))

@login_required(login_url='/')
def updateSchedule(request, id):
    if request.method == 'GET':
        obj_schedule = get_object_or_404(schedule, id=id)
        return render(request, 'schedule/update-schedule.html', {'schedule':obj_schedule})

    if request.method == 'POST':
        obj_schedule = get_object_or_404(schedule, id=id)
        obj_schedule.topic = request.POST.get('schedule_topic')
        obj_schedule.date = request.POST.get('schedule_date')
        obj_schedule.start_time = request.POST.get('schedule_start_time')
        obj_schedule.end_time = request.POST.get('schedule_end_time')
        obj_schedule.save()

        messages.success(request, 'SCHEDULE UPDATED SUCCESSFULLY')
        return HttpResponseRedirect(reverse('schedule:dashboard'))

@login_required(login_url='/')
def deleteSchedule(request, id):
    if request.method == 'GET':
        obj_schedule = get_object_or_404(schedule, id=id)
        obj_schedule.delete()
        messages.success(request, 'SCHEDULE DELETED SUCCESSFULLY')
        return HttpResponseRedirect(reverse('schedule:dashboard'))

def mark(request, id, val):
    if request.method == 'GET':
        obj_schedule = get_object_or_404(schedule, id=id)
        obj_schedule.completed = False if int(val) == 0 else True
        obj_schedule.save()
        msg = 'SCHEDULE MARKED INCOMPLETE SUCCESSFULLY' if int(val) == 0 else 'SCHEDULE MARKED COMPLETED SUCCESSFULLY'
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('schedule:dashboard'))