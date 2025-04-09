from django.contrib import admin
from .models import User, Event

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password", "date_joined")
    search_fields = ['username', 'email']
class EventAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "type")
    search_fields = ['user', 'name']

admin.site.register(User, UsersAdmin)
admin.site.register(Event, EventAdmin)