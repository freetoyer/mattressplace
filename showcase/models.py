from django.db import models
from django.urls import reverse
from decimal import Decimal
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
from django.utils.text import slugify
 
from ckeditor.fields import RichTextField


def image_folder(instance, filename):
    filename = f"{instance.slug}.{filename.split('.')[1]}"
    general_folder = instance.__class__.__name__
    if general_folder=='Product_Image':
        foldername = slugify(instance.product.title).capitalize()
    else:
        foldername = instance.slug
    return f"{general_folder}/{foldername}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_folder)
 
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    characteristics = RichTextField()
    description = RichTextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            self.slug = slug
        super().save(*args, **kwargs)


class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=image_folder)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    main_image = models.BooleanField(default=False)
     
    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.product.product_images:
                image_number = self.product.product_images.count() + 1
            else:
                image_number = 1
            slug = f"{self.product.slug}_{image_number}"
            self.slug = slug
            self.name = slug.capitalize()
        super().save(*args, **kwargs)
            

class Product_Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{self.product.slug}_{self.size}"
            self.slug = slug
            self.name = slug.capitalize()
        super().save(*args, **kwargs)


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_folder)
    description = RichTextField()

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class CatalogueFile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    file = models.FileField(upload_to=image_folder)
 
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        
    def __str__(self):
        return self.name



