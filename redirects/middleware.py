# -*- coding: utf-8 -*-

import django
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q

if django.VERSION < (1, 10):
    MiddlewareMixin = object
else:
    # https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
    from django.utils.deprecation import MiddlewareMixin

from redirects.models import Redirect


class RedirectMiddleware(MiddlewareMixin):
    @staticmethod
    def _find_response(redirects, match, path):
        redirects_list = filter(lambda obj: obj.match == match, redirects)
        for redirect_obj in redirects_list:
            redirect_response = redirect_obj.get_response(path)
            if redirect_response:
                return redirect_response
        return None

    def process_request(self, request):
        current_site = get_current_site(request)
        path = request.get_full_path()

        redirects_qs = Redirect.objects.filter(
            (Q(site=current_site) | Q(site__isnull=True)),
            (Q(match=Redirect.MATCH_EXACT) & Q(old_path__iexact=path))
            | Q(match=Redirect.MATCH_PREFIX)
            | Q(match=Redirect.MATCH_REGEX),
        )
        redirects_list = list(redirects_qs)

        return (
            self._find_response(redirects_list, Redirect.MATCH_EXACT, path)
            or self._find_response(redirects_list, Redirect.MATCH_PREFIX, path)
            or self._find_response(redirects_list, Redirect.MATCH_REGEX, path)
            or None
        )
