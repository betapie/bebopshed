from django.contrib import admin

from .models import Instrument, Artist, Progression, Album, Line

admin.site.register(Instrument)
admin.site.register(Artist)
admin.site.register(Progression)
admin.site.register(Album)
admin.site.register(Line)
