from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField



def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    general_folder = instance.__class__.__name__
    if general_folder=='Product_Image':
        foldername = slugify(instance.product.title).capitalize()
    else:
        foldername = instance.slug
    return '{0}/{1}/{2}'.format(general_folder, foldername, filename)

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})
 
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    characteristics = RichTextField()
    description = RichTextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

@receiver(pre_save, sender=Product)
def pre_save_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug


class Product_Image(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=image_folder)
    image_number = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.name
     
    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

@receiver(pre_save, sender=Product_Image)
def pre_save_product_image_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        product_images = Product_Image.objects.all() 
        if product_images:
            last_id_dict = product_images.order_by('-id').values('id')[0]
            image_number = last_id_dict['id'] + 1
        else:
            image_number = 1
        slug = instance.product.slug + '_' + str(image_number)
        name = slug.capitalize()
        instance.image_number = image_number
        instance.slug = slug
        instance.name = name



class Product_Size(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

@receiver(pre_save, sender=Product_Size)
def pre_save_product_size_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = instance.product.slug + '_' + instance.size
        name = slug.capitalize()
        instance.slug = slug
        instance.name = name



class Certificate(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(upload_to=image_folder)
    description = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

@receiver(pre_save, sender=Certificate)
def pre_save_certificate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name, allow_unicode=True)
        instance.slug = slug



class CatalogueFile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    file = models.FileField(upload_to=image_folder)

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#       return reverse('category_detail', kwargs={'category_slug': self.slug})
 
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def get_absolute_url(self):
        url = self.file.url
        path = url[1:]
        return reverse('catalogue_file_download', kwargs={'path': path})

