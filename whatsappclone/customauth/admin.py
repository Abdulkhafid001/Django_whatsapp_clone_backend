from django.contrib import admin
from .models import WcUser, WcRefreshToken


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')


admin.site.register(WcUser)
admin.site.register(WcRefreshToken, AccessTokenAdmin)
