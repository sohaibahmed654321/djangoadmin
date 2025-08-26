from django.contrib import admin
from . import models


admin.site.site_header ="ECOMMERCE"
admin.site.site_title = "Hamari App Ecommerce"
admin.site.index_title = "Dashboard"

admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.Contact)




# Register your models here.
