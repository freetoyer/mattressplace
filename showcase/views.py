from django.shortcuts import render
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate

from operator import attrgetter


def base_view(request):
    categories = Category.objects.all()
    certificates = Certificate.objects.all()
    context = {
            'categories': categories,
            'certificates': certificates
            }
    return render(request, 'base.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    product_images = Product_Image.objects.all()
    product_sizes = Product_Size.objects.all()
    products_sorted = sorted(products, key=attrgetter('slug'))
    product_images_sorted = sorted(product_images, key=attrgetter('slug'))
    
    prod_prod_images_dict = {}
    prod_images_list = []
    for product in products_sorted:
        prod_images_grouped = product.product_images.all()
        prod_images_grouped_sorted = tuple(sorted(prod_images_grouped, key=attrgetter('main_image'), reverse=True))
        prod_images_list.append(prod_images_grouped_sorted)
    prod_prod_images_dict = dict(zip(products_sorted, prod_images_list))
    
    context = {
            'categories': categories,
            'category': category,
            'products': products,
            'product_images': product_images,
            'prod_prod_images_dict': prod_prod_images_dict, 
            'product_sizes': product_sizes,
            } 
    return render(request, 'category.html', context)


def contacts_view(request):
    categories = Category.objects.all()
    context = {
            'categories': categories
            }
    return render(request, 'contacts.html', context)
