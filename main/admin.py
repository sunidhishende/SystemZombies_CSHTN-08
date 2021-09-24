from main.views import video
from django.contrib import admin
from .models import DevName,External, Video, Review

admin.site.register(DevName)
admin.site.register(Video)
admin.site.register(External)
admin.site.register(Review)
