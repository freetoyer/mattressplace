from django.shortcuts import render, redirect

import os
from operator import attrgetter

from mattressplace.settings import MEDIA_ROOT
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate, CatalogueFile


def base_view(request):
    return render(request, 'base.html')


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)
    cataloguefile = CatalogueFile.objects.get(slug='catalogue')
    context = {
            'category': category,
            'products': products,
            'cataloguefile': cataloguefile
            } 
    return render(request, 'category.html', context)


def certificates_view(request):
    certificates = Certificate.objects.all()
    cataloguefile = CatalogueFile.objects.get(slug='catalogue')
    context = {
            'certificates': certificates,
            'cataloguefile': cataloguefile
            }
    return render(request, 'certificates.html', context)


def contacts_view(request):
    cataloguefile = CatalogueFile.objects.get(slug='catalogue')
    context = {
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
