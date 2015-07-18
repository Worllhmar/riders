from django.shortcuts import render, get_list_or_404,  get_object_or_404
from blogs.models import Blog
from links.models import Link
from contact.models import Contact

def post(request, post):

    post = Blog.objects.get(url=post)
    links = Link.objects.all
    contacts = Contact.objects.all

    return render(request, 'post.html', {'post': post, 'links': links, 'contacts': contacts})