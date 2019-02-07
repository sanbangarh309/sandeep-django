from django.shortcuts import render
from django.http import HttpResponse

from .models import User,Project

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    projects = Project.objects.all()
    return render(request, "index.html",{"page":"Home","sandeep": user,"projects":projects})

def about(request):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    return render(request, "about.html",{"page":"About","sandeep": user})

def portfolio(request):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    projects = Project.objects.all()
    return render(request, "portfolio.html",{"page":"Portfolio","sandeep": user,"projects":projects})


def db(request):
    user = User()
    # User.objects.filter().delete()
    user.name = 'sandeep bangarh'
    user.email = 'sanbangarh309@gmail.com'
    user.phone = '9896747812'
    user.save()

    users = User.objects.all()

    return render(request, "db.html", {"greetings": users})
