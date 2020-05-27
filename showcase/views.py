from django.shortcuts import render
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate, CatalogueFile

from operator import attrgetter

import os
from mattressplace.settings import MEDIA_ROOT
from django.shortcuts import redirect


def base_view(request):
    categories = Category.objects.all()
    context = {
            'categories': categories
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
    
    cataloguefile = CatalogueFile.objects.get(slug__iexact='catalogue')

    context = {
            'categories': categories,
            'category': category,
            'products': products,
            'product_images': product_images,
            'prod_prod_images_dict': prod_prod_images_dict, 
            'product_sizes': product_sizes,
            'cataloguefile': cataloguefile
            } 
    return render(request, 'category.html', context)


def certificates_view(request):
    categories = Category.objects.all()
    certificates = Certificate.objects.all()
    cataloguefile = CatalogueFile.objects.get(slug__iexact='catalogue')
    context = {
            'categories': categories,
            'certificates': certificates,
            'cataloguefile': cataloguefile
            }
    return render(request, 'certificates.html', context)


def contacts_view(request):
    categories = Category.objects.all()
    cataloguefile = CatalogueFile.objects.get(slug__iexact='catalogue')
    context = {
            'categories': categories,
            'cataloguefile': cataloguefile
            }
    return render(request, 'contacts.html', context)


def download(request, path):
    file_path = os.path.join(MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
#            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            response.write(fh.read()) 
    return render(request, 'base.html')
#    return redirect('views.base_view')
