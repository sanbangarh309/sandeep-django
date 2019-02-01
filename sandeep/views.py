from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    user = Users()
    user.save()

    users = Users.objects.all()

    return render(request, "db.html", {"greetings": users})
