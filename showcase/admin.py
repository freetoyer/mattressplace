from django.contrib import admin
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate


class Product_Admin(admin.ModelAdmin):
    readonly_fields = ('slug', 'short_title')


class Product_Image_Admin(admin.ModelAdmin):
    readonly_fields = ('image_number', 'slug', 'name',)


class Product_Size_Admin(admin.ModelAdmin):
    readonly_fields = ('slug', 'name',)


class Certificate_Admin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category)
admin.site.register(Product, Product_Admin)
admin.site.register(Product_Image, Product_Image_Admin)
admin.site.register(Product_Size, Product_Size_Admin)
#admin.site.register(Size_Price)
admin.site.register(Certificate, Certificate_Admin)
