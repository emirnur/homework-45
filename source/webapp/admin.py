from django.contrib import admin
from webapp.models import Tracker


class TrackerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'status', 'deadline']
    list_filter = ['title', 'status']
    list_display_links = ['pk', 'title']
    search_fields = ['title', 'text']
    fields = ['title', 'text', 'status', 'deadline']
    readonly_fields = ['deadline']


admin.site.register(Tracker, TrackerAdmin)