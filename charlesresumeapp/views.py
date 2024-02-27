from django.shortcuts import render
from .models import MyInfo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messages = request.POST.get('messages')
        # message = request.POST.get('message')
        # job_title = request.POST.get('job_title')
        
        emp = MyInfo.objects.create(name=name,email=email,subject=subject,messages=messages)
    elif request.method == 'GET':
        return render(request, 'charlesresumeapp/index.html',{})
    return render(request, 'charlesresumeapp/index.html', {'emp':emp})

def about(request):
    return render(request, 'charlesresumeapp/about.html',{})


def experience(request):
    return render(request, 'charlesresumeapp/experience.html',{})


def service(request):
    return render(request, 'charlesresumeapp/service.html',{})


def portfolio(request):
    return render(request, 'charlesresumeapp/portfolio.html',{})


def contact(request):
    return render(request, 'charlesresumeapp/contact.html',{})

def resume(request):
    return render(request, 'charlesresumeapp/resume.html',{})