from django.contrib import admin

from profiles_api.models import ApiView, ProfileFeedItem, UserProfile

# Register your models here.

admin.site.register(ApiView)
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
