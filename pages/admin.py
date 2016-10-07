from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Page, PageAdmin)
