from django.db import models
from django.urls import reverse


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

