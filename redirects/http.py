from django.http import HttpResponseGone, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect as HttpResponseTemporaryRedirect
from django.http.response import HttpResponseRedirectBase


class HttpResponseSeeOtherRedirect(HttpResponseRedirectBase):
    status_code = 303


class HttpResponseStrictTemporaryRedirect(HttpResponseRedirectBase):
    status_code = 307


class HttpResponseStrictPermanentRedirect(HttpResponseRedirectBase):
    status_code = 308
