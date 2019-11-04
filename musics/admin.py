from django.contrib import admin

# Register your models here.
from .models import Artist, Music, Review

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Review)
