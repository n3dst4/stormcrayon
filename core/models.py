from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
import markdown
from django.dispatch import Signal


class FeaturedLink (models.Model):
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
        links_updated.send(sender=self)
        super(FeaturedLink, self).save()
        
    class Meta (object):
        ordering = ("sequence", "name")

links_updated = Signal(providing_args=[])        
from django.core.cache import cache
def trash_the_cache(sender, **kwargs):
    cache.clear()
links_updated.connect(trash_the_cache)
