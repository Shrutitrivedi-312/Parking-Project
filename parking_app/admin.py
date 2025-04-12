from django.contrib import admin
from .models import ParkingRequest, Guard

@admin.register(Guard)
class GuardAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact')
    search_fields = ('name', 'location')

@admin.register(ParkingRequest)
class ParkingRequestAdmin(admin.ModelAdmin):
    list_display = ('user_query', 'guard', 'timestamp', 'guard_reply')
    search_fields = ('user_query', 'guard__name', 'guard__location')
    list_editable = ('guard_reply',)  # Make the guard_reply field editable directly in the admin panel
