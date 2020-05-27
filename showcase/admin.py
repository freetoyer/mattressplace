from django.contrib import admin
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate, CatalogueFile


class Product_Admin(admin.ModelAdmin):
    readonly_fields = ('slug',)
#    prepopulated_fields = {'slug': ('title',)}


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
admin.site.register(Certificate, Certificate_Admin)
admin.site.register(CatalogueFile)
