from stormcrayon.core.models import FeaturedLink
from django.contrib import admin



class FeaturedLinkAdmin(admin.ModelAdmin):
    list_display = ("sequence", "live", "name", "category", "address",)
    list_display_links = ("name",)
    list_editable = ("sequence", "live")
    list_filter = ("category",)
    readonly_fields = ("description_html",)
    ordering = ("sequence", "name")

admin.site.register(FeaturedLink, FeaturedLinkAdmin)
