# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def post_view(request):
	return render(request, 'post/post_view.html', {})
