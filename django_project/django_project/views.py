from django.shortcuts import render, get_list_or_404
from blogs.models import Blog
from events.models import Event
from links.models import Link
from contact.models import Contact
from django.http import HttpResponse


 
def home(request):

    posts = list(Blog.objects.order_by('-date'))[:10]
    next_events = list(Event.objects.order_by('-dateTime'))[:1]
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'home.html', {'posts': posts, 'next_events': next_events, 'links': links, 'contacts': contacts})

