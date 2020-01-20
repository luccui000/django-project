# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save

from economic.utils import  create_new_order_id_generator
from carts.models import Cart

ORDER_STATUS_CHOICE = (
	('created', 'Created'),
	('paid', 'Paid'),
	('shipped', 'Shipped'),
	('refunded', 'Refunded'),
	)


# Create your models here.

class Order(models.Model):
	order_id  		= models.CharField(max_length=120, blank=True)
	# 
	cart 			= models.ForeignKey(Cart)
	# 
	status			= models.CharField(max_length=120, choices=ORDER_STATUS_CHOICE)
	# 
	shipped_total	= models.DecimalField(default=3.99, max_digits=20, decimal_places=2)
	# 
	total			= models.DecimalField(default=5.99, max_digits=20, decimal_places=2)

	def __str__(self):
		return self.order_id

	def update_total(self):
		cart_total 		= self.cart.total
		shipped_total   = self.shipped_total
		new_total 		= cart_total + shipped_total
		self.total 		= new_total
		self.save()
		return new_total



def pre_save_new_order_id(instance, sender, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = create_new_order_id_generator(instance)

pre_save.connect(pre_save_new_order_id, sender=Order)

def post_save_order(instance, sender, created, *args, **kwargs):
	if not created:
		cart_obj 	= instance
		cart_total 	= cart_obj.total
		cart_id 	= cart_obj.id

		qs 			= Order.objects.filter(cart__id=cart_id)

		if qs.counter() == 1:
			order_obj = qs.first()
			order_obj.save()

post_save.connect(post_save_order, sender=Cart)

def post_save_order(instance, sender, created, *args, **kwargs):
	if created:
		instance.update_total()

post_save.connect(post_save_order, sender=Order)
