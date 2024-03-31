from django.contrib import admin

# Register your models here.
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'creator', 'created_at']

 


