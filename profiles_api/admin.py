from django.contrib import admin

from profiles_api.models import ApiView, UserProfile

# Register your models here.

admin.site.register(ApiView)
admin.site.register(UserProfile)
