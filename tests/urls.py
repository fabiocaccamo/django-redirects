# -*- coding: utf-8 -*-

import django

from django.contrib import admin

if django.VERSION < (2, 0):
    from django.conf.urls import include, url as re_path
else:
    from django.urls import include, re_path

from django.http import HttpResponse


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(
        r"^landing-301/$",
        lambda x: HttpResponse(),
        name="redirected-301",
    ),
    re_path(
        r"^landing-302/$",
        lambda x: HttpResponse(),
        name="redirected-302",
    ),
    re_path(
        r"^landing-303/$",
        lambda x: HttpResponse(),
        name="redirected-303",
    ),
    re_path(
        r"^landing-307/$",
        lambda x: HttpResponse(),
        name="redirected-307",
    ),
    re_path(
        r"^landing-308/$",
        lambda x: HttpResponse(),
        name="redirected-308",
    ),
]
