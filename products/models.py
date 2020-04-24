from django.db import models
from django.urls import reverse 
# Create your models here.


class Product(models.Model):
    title = models.CharField( max_length=50,blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    active = models.BooleanField()

    def get_link(self,*args, **kwargs):
        return reverse("products:product-details",kwargs={"id":self.id})