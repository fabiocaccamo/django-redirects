# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirectBase


class HttpResponseStrictPermanentRedirect(HttpResponseRedirectBase):
    status_code = 308


class HttpResponseSeeOtherRedirect(HttpResponseRedirectBase):
    status_code = 303


class HttpResponseStrictTemporaryRedirect(HttpResponseRedirectBase):
    status_code = 307
