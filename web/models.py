from django.db import models


class WebApplication(models.Model):
    title = models.CharField(blank=False, null=False, max_length=254)
    counter = models.IntegerField(default=0)
    counter_limit = models.IntegerField(default=300)
