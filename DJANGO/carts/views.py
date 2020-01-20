# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.middleware.csrf import CsrfViewMiddleware

from .models import Cart
from products.models import Product

# Create your views here.

def cart_view(request):
	cart_obj, new_cart = Cart.objects.new_or_get(request)
	content = {
		"cart": cart_obj
	}
	return render(request, 'cart/view.html', content)

def cart_update(request):
	products_id = request.POST.get('product_id')
	if products_id is not None:
		try:
			products_obj = Product.objects.get(id=products_id)

		except products_id.DoesNotExist:
			print("Khong tim thay id")
			return redirect('products:list')
			
		# products_obj = get_object_or_404(Product, id=products_id)
		cart_obj, new_cart = Cart.objects.new_or_get(request)

		if products_obj in cart_obj.products.all():
			cart_obj.products.remove(products_obj)
		else:
			cart_obj.products.add(products_obj)

		request.session['cart_items'] = cart_obj.products.count()
		print(request.session['cart_items'])

	return redirect('cart:home')

