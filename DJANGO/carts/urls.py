from django.conf.urls import url

from .views import (
        cart_view,
        cart_update,
        )

urlpatterns = [
    url(r'^$', cart_view, name='home'),
    url(r'^update/$', cart_update, name='update'),
]
