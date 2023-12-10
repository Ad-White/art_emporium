from django.shortcuts import redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import SubscribedUsers


def subscribe(request):
    """ Add's the name and email address of a user
    wanting to subscribe to the sites newsletter """
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, 'Please ensure the form is \
                 filled out correctly.')
            return redirect("/")

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request, f"Sorry, {email}. This email address is already \
                    subscribed.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

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
