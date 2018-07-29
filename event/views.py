from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Event

def index(request):
    latest_event_list = Event.objects.order_by('-date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'event/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants = event.participant_set.all()
    context = {
        'event': event,
        'participants': participants,
    }
    # print(str(participants.))
    return render(request, 'event/detail.html', context)
