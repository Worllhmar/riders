from django.shortcuts import render, get_list_or_404
from contact.models import Contact
from links.models import Link
from contact.models import Contact

def contact(request):

    contacts = list(Contact.objects.order_by('name'))
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'contacto.html', {'contacts': contacts, 'links': links, 'contacts': contacts})
