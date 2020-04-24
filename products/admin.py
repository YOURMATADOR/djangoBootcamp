from django.contrib import admin

from .models import Product

# ? add the model to the admin page 
admin.site.register(Product)
# Register your models here.
