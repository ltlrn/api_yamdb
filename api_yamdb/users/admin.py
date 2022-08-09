from django.contrib import admin

from .models import User

class AdminUser(admin.ModelAdmin):
    list_display = ['bio', 'role']

admin.site.register(User, AdminUser)
