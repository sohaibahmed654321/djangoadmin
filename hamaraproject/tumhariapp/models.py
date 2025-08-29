from django.db import models
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="brands/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # ✅ description added
    image = models.ImageField(upload_to="categories/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # ✅ description added
    quantity = models.PositiveIntegerField(default=0)  # ✅ quantity added
    is_available = models.BooleanField(default=True)  # ✅ availability added
    size = models.CharField(max_length=50, null=True, blank=True)  # ✅ size added
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to="contacts/", null=True, blank=True)

    def __str__(self):
        return self.name

#abhi

# User-submitted Contact Form
class Contaact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name} - {self.email}"
