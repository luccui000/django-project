# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from decimal import  Decimal
from django.dispatch import receiver


from products.models import Product

User = settings.AUTH_USER_MODEL

# Cart Manager { new_or_get | new }
class CartMananger(models.Manager):

	def new_or_get(self, request):
		cart_id = request.session.get('cart_id', None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_cart = False
			cart_obj = qs.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_cart = True
			request.session['cart_id'] = cart_obj.id

		return cart_obj, new_cart
		
	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.create(user=user_obj)

	
# Cart 
class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True)
	products	= models.ManyToManyField(Product, blank=True)
	total		= models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
	subtotal	= models.DecimalField(default=0.00, max_digits=20, decimal_places=2)	
	update		= models.DateTimeField(auto_now=True)
	post_time	= models.DateTimeField(auto_now_add=True)

	objects 	= CartMananger()

	def __str__(self):
		return str(self.id)


# Update Subtotal Price
def m2m_changed_save_receiver(sender, instance, action, *args, **kwargs):
	if action == 'post_add' or action == 'post_remove' or action == 'post_clean':
		products = instance.products.all()
		total = 0
		for x in products:
			total += x.price
	  	if instance.subtotal != total:
			instance.subtotal = total
			instance.save()

m2m_changed.connect(m2m_changed_save_receiver, sender=Cart.products.through)

# Update Total Price
def pre_save_card_receiver(sender, instance, *args, **kwargs):
	if instance.subtotal > 0:
		instance.total = Decimal(instance.subtotal ) * Decimal(1.02)
	else:
		instance.total = 0.0

post_save.connect(pre_save_card_receiver, sender=Cart)