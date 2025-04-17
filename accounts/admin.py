from django.contrib import admin
from .models import UserProfile, UserProfileAddress


admin.site.register(UserProfile)
admin.site.register(UserProfileAddress)
