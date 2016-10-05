from django.db import models

class Page(models.Model):
    """Website Pages."""
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField()
    slug = models.URLField(null=False, blank=False)
    meta_keywords = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.CharField(max_length=254, null=True, blank=True)

def __str__(self):
    return self.title
