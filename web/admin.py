from django.contrib import admin
from web.models import WebApplication

class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'counter')

admin.site.register(WebApplication, WebAdmin)
