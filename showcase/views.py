from django.shortcuts import render
from showcase.models import Category

def base_view(request):
    categories = Category.objects.all()
    context = {
            'categories': categories
            }
    return render(request, 'base.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, 'category.html', {'category': category})
