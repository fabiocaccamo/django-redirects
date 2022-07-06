# -*- coding: utf-8 -*-

from django.http import (
    HttpResponseGone,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect as HttpResponseTemporaryRedirect,
)
from django.http.response import HttpResponseRedirectBase


class HttpResponseSeeOtherRedirect(HttpResponseRedirectBase):
    status_code = 303


class HttpResponseStrictTemporaryRedirect(HttpResponseRedirectBase):
    status_code = 307


class HttpResponseStrictPermanentRedirect(HttpResponseRedirectBase):
    status_code = 308
