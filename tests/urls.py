from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path(
        "landing-301/",
        lambda x: HttpResponse(),
        name="redirected-301",
    ),
    path(
        "landing-302/",
        lambda x: HttpResponse(),
        name="redirected-302",
    ),
    path(
        "landing-303/",
        lambda x: HttpResponse(),
        name="redirected-303",
    ),
    path(
        "landing-307/",
        lambda x: HttpResponse(),
        name="redirected-307",
    ),
    path(
        "landing-308/",
        lambda x: HttpResponse(),
        name="redirected-308",
    ),
]
