from django.contrib import admin

from .models import Artists


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'profile_info',
    )

    ordering = ('artist',)


admin.site.register(Artists, ArtistsAdmin)
