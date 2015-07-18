from django.shortcuts import render, get_list_or_404,  get_object_or_404
from riders.models import Rider
from links.models import Link
from contact.models import Contact

def riders_fmx_list(request):

    riders = list(Rider.objects.filter(tipo='fmx'))
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'riders.html', {'riders': riders, 'links': links, 'contacts': contacts})

def riders_bmx_list(request):

    riders = list(Rider.objects.filter(tipo='bmx'))
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'riders.html', {'riders': riders, 'links': links, 'contacts': contacts})

def rider(request, rider):

    rider = Rider.objects.get(url=rider)
    links = Link.objects.all
    contacts = Contact.objects.all
    images = rider.images.all

    return render(request, 'rider.html', {'rider': rider, 'links': links, 'contacts': contacts, 'images': images})
