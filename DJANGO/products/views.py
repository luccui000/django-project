from django.shortcuts import render, get_object_or_404
from django.core.exceptions import MultipleObjectsReturned
from django.views.generic import ListView, DetailView
from django.http import Http404
# from django.views.generic import ArchiveIndexView

from .models import Product
from carts.models import Cart

# Create your views here.

#  --------------------  Class --------------------

# List View

class ProductListView(ListView):
    queryset = Product.objects.all()
    # model = Product
    template_name = "products/list.html"
    # def get_context_data(self, *args, **kwargs):
    #     context  = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_queryset(self):
        request = self.request
        return Product.objects.all()


# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = "products/products_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ListViewProducts, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# def get_data(request):
#     queryset = Product.objects.all()
#     content = {
#         'qs' : queryset
#     }
#     return render(request, 'products/products_list.html', content)


# Detail List View

class ProductDetailListView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context  = super(ProductDetailListView, self).get_context_data(*args, **kwargs)
        return context
    def get_objects(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("San pham khong ton tai")
        return instance

# Feature List View & Detail View

class ProductFeatureListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductsFeatureDetailView(DetailView):

    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_cart = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("UHMMMM")

        return instance


# -------------------- def --------------------

def product_detail_listview(request, pk=None, *args, ** kwargs):
    instance = Product.objects.all()
    # instance = get_object_or_404(Product, pk=pk)
    context = {
        'object' : instance
    }
    return render(request, 'products/list.html', context)
