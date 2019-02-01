from django.shortcuts import render
from django.http import HttpResponse

from .models import Users

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def db(request):
    user = Users()
    # Users.objects.filter().delete()
    user.name = 'sandeep bangarh'
    user.email = 'sanbangarh309@gmail.com'
    user.phone = '9896747812'
    user.save()

    users = Users.objects.all()

    return render(request, "db.html", {"greetings": users})
