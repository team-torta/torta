from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Event, Participant
from .forms import EventForm

def index(request):
    event_list = Event.objects.order_by('-date')
    # participant_no = Participant.objects.filter(participant__event=self).count()
    context = {'event_list': event_list}
    return render(request, 'event/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants = event.participant_set.all()
    context = {
        'event': event,
        'participants': participants,
    }
    return render(request, 'event/detail.html', context)

def add(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        Event.objects.create(**form.cleaned_data)
        # form.save()
        return redirect('event:index')
    context = {
        'form': form,
    }
    return render(request, 'event/add.html', context)

# def get_participant_no(self):
#     return Participant.objects.filter(participant__event=self).count()
#     return Event.objects.filter(event__participant=self).count()
