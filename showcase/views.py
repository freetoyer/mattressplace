from django.shortcuts import render, redirect

import os
from operator import attrgetter

from mattressplace.settings import MEDIA_ROOT
from showcase.models import Category, Product, Product_Image, Product_Size, Certificate, Contacts, CatalogueFile


def base_view(request):
    return render(request, 'base.html')


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)
    context = {
            'category': category,
            'products': products,
            } 
    return render(request, 'category.html', context)


def certificates_view(request):
    certificates = Certificate.objects.all()
    context = {
            'certificates': certificates,
            }
    return render(request, 'certificates.html', context)


def contacts_view(request):
    context = {
            'contacts': Contacts.objects.all()[0]
            }
    return render(request, 'contacts.html', context)
