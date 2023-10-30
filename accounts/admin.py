from django.contrib import admin

# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)

<<<<<<< HEAD
# admin.register(CustomUser)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined')
=======
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
