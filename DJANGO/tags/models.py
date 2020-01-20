# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product

from products.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Tag(models.Model):
	#
	title		= models.CharField(max_length=200)
	#
	slug  		= models.SlugField()
	#
	post_times	= models.DateTimeField(auto_now_add=True)
	#
	active		= models.BooleanField(default=True)
	#
	products 	=models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return self.title

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Tag)