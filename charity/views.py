from django.shortcuts import render
import datetime
from .models import events

# Create your views here.
site = "SHEAVES OF HOPE FOUNDATION | "
def index(request):    
    page = "Home"
    return render(request,'index.html', {'page': page,'site':site})

def about(request):
    page = "About"
    date = datetime.date.today()
    return render(request,'about.html', {'page': page,'site':site, 'today':date,})

def gallery(request):
    page = "Gallery"
    return render(request,'gallery.html', {'page': page,'site':site})

def projects(request):
    page = "Projects"
    return render(request,'project.html', {'page': page,'site':site})

def contact(request):
    page = "Get in Touch"
    return render(request,'contact.html', {'page': page,'site':site})

def recents(request):
    recent_events_list = events.objects.order_by('event_date')[:5]
    context = {'recent_events_list': recent_events_list}
    return render(request, 'base.html', {'recent': context}) 