from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save
from django.db.models import Q

from economic.utils import unique_slug_generator
import random
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Tao ten random cho hinh anh Upload len
def lay_file(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def tai_len_file_image(instance, filename):
    new_filename = random.randint(1000000, 999999999999)
    name, ext    = lay_file(filename)
    final_filename     = '{new_filename}_{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
     )

class ProductQuerySet(models.query.QuerySet):
    def features(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)
    def search(self, query):
        lookups = (Q(title__icontains=query)|
                  Q(description__icontains=query)|
                  Q(price__icontains=query)|
                  Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def featured(self):                       # Product.objects.= self.get_queryset()
        return self.get_queryset().features()
    def all(self):
        return self.get_queryset().active()

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_id(self, id):
        queryset = self.get_queryset().filter(id=id)
        if queryset.count() == 1:
            return queryset.first()
        return None
    def search(self, query):
        return self.get_queryset().search(query)


class Product(models.Model):
    # Tieu de san pham
    title           = models.CharField(max_length=120)
    # tu khoa tim kiem
    slug            = models.SlugField(blank=True, unique=True)
    # Mo ta san pham
    description     = models.TextField()
    # Gia san pham
    price           = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    # Hinh san pham
    image           = models.ImageField(upload_to=tai_len_file_image, null=True, blank=True)
    # Thoi gian dang bai
    post_times      = models.DateTimeField(auto_now_add=True)
    # San pham khac
    featured        = models.BooleanField(default=False)
    # Trang thai san pham
    active          = models.BooleanField(default=True)


    objects        = ProductManager()

    # slug            = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
            # return "/products/{slug}/".format(slug=self.slug)
            return reverse('products:detail', kwargs = {'slug': self.slug })
    # def get_absolute_url(self):
    #     return reverse('products', kwargs={'slug': self.slug})
    #
    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title

# tao chuyen muc san pham

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
