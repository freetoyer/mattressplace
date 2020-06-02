from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.base_view, name='base'),
    # re_path(r'^category/(?P<category_slug>\w+)/$', views.category_view, name='category_detail'),
    path('category/<slug:category_slug>/', views.category_view, name='category_detail'),
    path('certificates', views.certificates_view, name='certificates'),
    path('contacts', views.contacts_view, name='contacts'),
]

urlpatterns += staticfiles_urlpatterns()
