from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from home.models import Photo, Person, PersonGallery
import re
# ReGEx required for getting photo name
post_type = re.compile(r"static/images/(.*)")
# Create your views here.
def landing(request):
    return render(request, "landing.html")
def loginUser(request):
    pass

def index(request):
    pass

def loginUser(request):
    pass

def logoutUser(request):
    pass

def registerUser(request):
    pass

def registerUser2(request):
    pass

def process(request):
    pass