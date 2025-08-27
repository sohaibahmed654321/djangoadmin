from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Brand, Category, Contact


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website', 'thumbnail', 'created_at')
    search_fields = ('name', 'description')

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
    list_display = ('name', 'description', 'thumbnail', 'created_at')
    search_fields = ('name', 'description')

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
    list_display = (
        'name', 'brand', 'category', 'thumbnail',
        'price', 'quantity', 'is_available', 'size', 'description', 'created_at'
    )
    search_fields = ('name', 'description')
    list_filter = ('brand', 'category', 'is_available')
    list_editable = ('price', 'quantity', 'is_available', 'size')  # ✅ quick edit

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
    list_display = ('name', 'email', 'phone', 'message', 'thumbnail')
    search_fields = ('name', 'email', 'phone')

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"
    thumbnail.short_description = 'Image'
