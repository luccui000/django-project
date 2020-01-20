"""economic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import  home_page, about_page, contact_page, login_page, register_page, logout_view  # AuthorCreate


urlpatterns = [
    url(r'^admin/', admin.site.urls ),
    url(r'^$', home_page, name='home'),                     # goi den home page
    url(r'^about/$', about_page, name='about'),              # goi den about page
    url(r'^contact/$', contact_page, name='contact'),        # goi den ham contact page
    url(r'^login/$', login_page, name='login'),              # login page
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^post/', include("Post.urls"), name='post'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_page, name='register'),     # register page
    url(r'^boostrap/$', TemplateView.as_view(template_name= 'boostrap/example.html')),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("Search.urls", namespace='search')),
    # url(r'products/$', ProductListView.as_view() ),
    # url(r'products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='products'),
    # # url(r'products/(?P<pk>\d+)/$', ProductDetailListView.as_view(), name='product'),
    # url(r'featured/$', ProductFeatureListView.as_view(), name='feature'),
    # url(r'featured/(?P<pk>\d+)/$', ProductsFeatureDetailView.as_view(), name='featured'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
