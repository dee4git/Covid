from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    """views the home page"""
    return render(request, "home.html", {
    })