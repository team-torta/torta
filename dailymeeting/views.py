from django.shortcuts import render

from .models import Day

def index(request):
    day_list = Day.objects.order_by('-day')[:5]
    context = {'day_list': day_list}
    return render(request, 'dailymeeting/index.html', context)
