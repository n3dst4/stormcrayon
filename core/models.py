from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
import markdown
from django.dispatch import Signal
import re


class FeaturedLink (models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description_markdown = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = ImageWithThumbnailsField(
        upload_to="featured_link_images",
        blank=True,
        generate_on_save=True,
        thumbnail= {
            "size": (380, 320),
            "quality": 95,
            "options": {"crop": ",0"},
        }
    )
    image_address = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, choices=(
        ("sites", "Website I made"),
        ("other", "Other project I've done"),
    ))
    live = models.BooleanField(null=False, default=False)
    sequence = models.IntegerField(default=0)
    
    def save(self):
        foo = "\n[url]: /frame/" + str(self.id)
        self.description_html = markdown.markdown(self.description_markdown + foo)
        try:
            self.id = self.calculate_id()
        except e:
            pass # we're probably migrating
        links_updated.send(sender=self)
        super(FeaturedLink, self).save()
        
    def calculate_id(self):
        id = self.name.lower()
        id = id.replace("'", "");
        return re.sub(r'[^a-z0-9]+', '-', id).strip('-')
        
    class Meta (object):
        ordering = ("sequence", "name")

links_updated = Signal(providing_args=[])        
from django.core.cache import cache
def trash_the_cache(sender, **kwargs):
    cache.clear()
links_updated.connect(trash_the_cache)
