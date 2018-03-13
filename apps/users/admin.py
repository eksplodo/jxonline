from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'address', 'birthday', 'gender']
    search_fields = ['nickname', 'address', 'birthday', 'gender']
    list_filter = ['nickname', 'address', 'birthday', 'gender']

admin.site.register(UserProfile, UserProfileAdmin)