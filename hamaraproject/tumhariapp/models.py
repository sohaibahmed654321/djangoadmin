from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField( max_length=100)
    desc = models.CharField( max_length=100)
    website = models.URLField( blank=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField( max_length=100)
    desc = models.CharField( max_length=100)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField( max_length=100)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.IntegerField( )
    is_available = models.BooleanField(default=False)
    size = models.CharField(max_length=100)
    rating = models.DecimalField( max_digits=10, decimal_places=2)
    brandid = models.ForeignKey(Brand, on_delete=models.CASCADE)
    catid = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( max_length=100)
    phone = models.CharField( max_length=100)
    message = models.TextField( blank=True)

    def __str__(self):
        return self.name


