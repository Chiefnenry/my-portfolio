from django.urls import path
from .views import index,about,experience,service,portfolio,contact,resume

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('experience', experience, name='experience'),
    path('service', service, name='service'),
    path('portfolio', portfolio, name='portfolio'),
    path('contact', contact, name='contact'),
     path('resume', resume, name='resume'),
]