from django.contrib import admin
from showcase.models import Category, Product, Product_Image, Product_Size, Size_Price

class Product_Image_Admin(admin.ModelAdmin):
    readonly_fields = ('slug', 'name',)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_Image, Product_Image_Admin)
admin.site.register(Product_Size)
admin.site.register(Size_Price)
