from django.contrib import admin
from .models import User, Event, Chat

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password", "date_joined")
    search_fields = ['username', 'email']
class EventAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "type")
    search_fields = ['user', 'name']
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "sender", "message", "created_at")
    search_fields = ['event', 'sender']

admin.site.register(User, UsersAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Chat, ChatAdmin)