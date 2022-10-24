# -*- coding: utf-8 -*-

import django

if django.VERSION < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse

from django.http import HttpResponseNotFound
from django.test import Client, RequestFactory, TestCase

from redirects.models import Redirect


class ModelsTestCase(TestCase):
    """
    This class describes a models test case.
    """

    def setUp(self):
        self._client = Client()
        self._request_factory = RequestFactory()

    def test_redirect_type_choices(self):
        self.assertEqual(Redirect.TYPE_301, 301)
        self.assertEqual(Redirect.TYPE_302, 302)
        self.assertEqual(Redirect.TYPE_303, 303)
        self.assertEqual(Redirect.TYPE_307, 307)
        self.assertEqual(Redirect.TYPE_308, 308)

    def test_redirect_match_choices(self):
        self.assertEqual(Redirect.MATCH_EXACT, "exact")
        self.assertEqual(Redirect.MATCH_PREFIX, "prefix")
        self.assertEqual(Redirect.MATCH_REGEX, "regex")

    def test_redirect_301_url_and_status_code(self):
        Redirect.objects.create(
            old_path="/obsolete/page-301/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
        )
        response = self._client.get("/obsolete/page-301/")
        self.assertEqual(response.url, reverse("redirected-301"))
        self.assertEqual(response.status_code, 301)

    def test_redirect_302_url_and_status_code(self):
        Redirect.objects.create(
            old_path="/obsolete/page-302/",
            new_path=reverse("redirected-302"),
            type_status_code=Redirect.TYPE_302,
        )
        response = self._client.get("/obsolete/page-302/")
        self.assertEqual(response.url, reverse("redirected-302"))
        self.assertEqual(response.status_code, 302)

    def test_redirect_303_url_and_status_code(self):
        Redirect.objects.create(
            old_path="/obsolete/page-303/",
            new_path=reverse("redirected-303"),
            type_status_code=Redirect.TYPE_303,
        )
        response = self._client.get("/obsolete/page-303/")
        self.assertEqual(response.url, reverse("redirected-303"))
        self.assertEqual(response.status_code, 303)

    def test_redirect_307_url_and_status_code(self):
        Redirect.objects.create(
            old_path="/obsolete/page-307/",
            new_path=reverse("redirected-307"),
            type_status_code=Redirect.TYPE_307,
        )
        response = self._client.get("/obsolete/page-307/")
        self.assertEqual(response.url, reverse("redirected-307"))
        self.assertEqual(response.status_code, 307)

    def test_redirect_308_url_and_status_code(self):
        Redirect.objects.create(
            old_path="/obsolete/page-308/",
            new_path=reverse("redirected-308"),
            type_status_code=Redirect.TYPE_308,
        )
        response = self._client.get("/obsolete/page-308/")
        self.assertEqual(response.url, reverse("redirected-308"))
        self.assertEqual(response.status_code, 308)

    def test_redirect_match_exact(self):
        Redirect.objects.create(
            old_path="/obsolete-match-exact/page-301/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
            match=Redirect.MATCH_EXACT,
        )
        response = self._client.get("/obsolete-match-exact/page-301/")
        self.assertEqual(response.url, reverse("redirected-301"))

    def test_redirect_match_exact_with_wrong_url(self):
        Redirect.objects.create(
            old_path="/obsolete-match-exact/page-301/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
            match=Redirect.MATCH_EXACT,
        )
        response = self._client.get("/obsolete-match-exact/page-30X/")
        self.assertTrue(isinstance(response, HttpResponseNotFound))

    def test_redirect_match_prefix(self):
        Redirect.objects.create(
            old_path="/obsolete-match-prefix/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
            match=Redirect.MATCH_PREFIX,
        )
        response = self._client.get("/obsolete-match-prefix/page-301/")
        self.assertEqual(response.url, reverse("redirected-301"))

    def test_redirect_match_prefix_with_wrong_url(self):
        Redirect.objects.create(
            old_path="/ooobsolete-match-prefix/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
            match=Redirect.MATCH_PREFIX,
        )
        response = self._client.get("/obsolete-match-prefix/page-301/")
        self.assertTrue(isinstance(response, HttpResponseNotFound))

    def test_redirect_301_url_and_status_code(self):
        redirect_obj = Redirect.objects.create(
            old_path="/obsolete/page-counter/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
        )
        for i in range(0, 5):
            response = self._client.get("/obsolete/page-counter/")
        self.assertEqual(Redirect.objects.get(pk=redirect_obj.pk).counter, 5)
