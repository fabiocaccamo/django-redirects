from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, re_path

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
