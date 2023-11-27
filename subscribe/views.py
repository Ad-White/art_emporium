from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import SubscribedUsers


# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, 'Please fill out both input boxes')
            return redirect("/")

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(
            request, f'{email} was successfully subscribed to our newsletter!')
        return redirect("/")
