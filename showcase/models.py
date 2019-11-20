from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instance.slug, filename)

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=image_folder)
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Product_Image)
def pre_save_product_image_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        pre_save_product_image_slug.counter += 1
        slug = slugify(instance.product.title) + '_' + str(pre_save_product_image_slug.counter)
        name = slug.upper()
        instance.slug = slug
        instance.name = name

pre_save_product_image_slug.counter = 0


class Product_Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.CharField(max_length=10)


class Size_Price(models.Model):
    size = models.OneToOneField(Product_Size, on_delete=models.CASCADE, related_name='price_of_size')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
