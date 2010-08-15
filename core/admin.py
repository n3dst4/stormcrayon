from stormcrayon.core.models import FeaturedLink
from django.contrib import admin



class FeaturedLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "address")
    readonly_fields = ("description_html",)

admin.site.register(FeaturedLink, FeaturedLinkAdmin)
