from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
import markdown
from django.dispatch import Signal
import re
from cms.models import CMSPlugin

class FeaturedLink (CMSPlugin):
    slug = models.CharField(max_length=255, unique=True)
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
        foo = "\n[url]: /frame/" + str(self.slug)
        self.description_html = markdown.markdown(self.description_markdown + foo)
        try:
            self.slug = self.calculate_slug()
        except Exception:
            pass # we're probably migrating
        links_updated.send(sender=self)
        super(FeaturedLink, self).save()
        
    def calculate_slug(self):
        slug = self.name.lower()
        slug = slug.replace("'", "");
        return re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
        
    def __unicode__(self):
        return self.name        
        
    class Meta (object):
        ordering = ("sequence", "name")

links_updated = Signal(providing_args=[])        
from django.core.cache import cache
def trash_the_cache(sender, **kwargs):
    cache.clear()
links_updated.connect(trash_the_cache)


#class FeaturedLinkPlugin (CMSPlugin):
#    link = models.ForeignKey(FeaturedLink)
    
#import cms_plugins

















