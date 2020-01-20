from django.conf.urls import url

from .views import post_view

urlpatterns = [
    url(r'^$', post_view, name='post'),
]
