from django.contrib import admin

# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)

# admin.register(CustomUser)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined')
