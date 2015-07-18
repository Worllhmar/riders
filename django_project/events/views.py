from django.shortcuts import render, get_list_or_404, get_object_or_404
from events.models import Event
from links.models import Link
from contact.models import Contact

from django.http import HttpResponse

def events_list(request):

    #events = get_list_or_404(Event.objects.order_by('-dateTime'))
    events = Event.objects.all().order_by('-dateTime')
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'events.html', {'events': events, 'links': links, 'contacts': contacts})


def event(request, event):

    event = Event.objects.get(url=event)
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'events-detail.html', {'event': event, 'links': links, 'contacts': contacts})
