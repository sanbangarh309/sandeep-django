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
    # user = User.objects.get(pk=1)
    projects = Project.objects.all()
    print(projects)
    return render(request, "index.html",{"sandeep": user,"projects":projects})

def db(request):
    user = User()
    # User.objects.filter().delete()
    user.name = 'sandeep bangarh'
    user.email = 'sanbangarh309@gmail.com'
    user.phone = '9896747812'
    user.save()

    users = User.objects.all()

    return render(request, "db.html", {"greetings": users})
