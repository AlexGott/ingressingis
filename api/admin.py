from django.contrib import admin
from .models import GEOPoint, File


class ApiAdmin(admin.ModelAdmin):
    autocomplete_fields = ['name']
    search_fields = ['name']
    list_display = ['name','lat','lng']


admin.site.register(GEOPoint)