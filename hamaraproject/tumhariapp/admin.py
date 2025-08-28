from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Brand, Category, Contact, Contaact


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'thumbnail', 'created_at')
    search_fields = ('name',)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "website", "description")}),
        ("Media", {"fields": ("image",)}),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = 'Logo'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail', 'created_at')
    search_fields = ('name',)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description")}),
        ("Media", {"fields": ("image",)}),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = 'Image'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'thumbnail', 'price', 'quantity', 'is_available', 'created_at')
    search_fields = ('name', 'brand__name', 'category__name')
    list_filter = ('brand', 'category', 'is_available')

    fieldsets = (
        ("Basic Info", {"fields": ("name", "brand", "category", "description")}),
        ("Inventory", {"fields": ("price", "quantity", "size", "is_available")}),
        ("Media", {"fields": ("image",)}),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = 'Image'



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'thumbnail')
    search_fields = ('name', 'email', 'phone')

    fieldsets = (
        ("Contact Info", {"fields": ("name", "email", "phone", "message")}),
        ("Media", {"fields": ("image",)}),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = 'Image'

from django.contrib import admin
from .models import Contact

#abhi

@admin.register(Contaact)
class ContaactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
