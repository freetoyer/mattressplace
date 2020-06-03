from django import template

from ..models import Category, CatalogueFile, Slide
  
  
register = template.Library()  
  
  
@register.simple_tag  
def get_categories():  
    return Category.objects.annotate()


@register.simple_tag  
def get_cataloguefile_url():
    cataloguefile_url = CatalogueFile.objects.get(slug='catalogue').file.url
    return cataloguefile_url


@register.simple_tag  
def get_slides():  
    return Slide.objects.annotate()