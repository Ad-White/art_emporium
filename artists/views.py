from django.shortcuts import render
from .models import Artists


def all_artists(request):
    """ A view to show all artists """

    artists = Artists.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)
