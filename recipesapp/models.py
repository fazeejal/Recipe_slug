from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)
    ingredients = models.TextField(blank=False, null=False)
    instructions = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null = True, blank=True, unique=True)

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)