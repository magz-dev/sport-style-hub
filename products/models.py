from django.db import models
from profiles.models import UserProfile
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
 

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey(UserProfile, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    review_text = models.TextField([MaxLengthValidator(limit_value=500)], max_length=500, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
