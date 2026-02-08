from django.contrib import admin
from .models import WcUser, AccessToken


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')


admin.site.register(WcUser)
admin.site.register(AccessToken, AccessTokenAdmin)
