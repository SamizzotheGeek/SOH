from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'sohf'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about' ),
    path('gallery/',views.gallery, name='gallery' ),
    path('projects/',views.projects, name='projects' ),
    path('contact/',views.contact, name='contact' ),
    path('<int:events_id>/', views.events, name='events'), 


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
