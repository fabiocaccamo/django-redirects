from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from redirects.models import Redirect


class AdminTestCase(TestCase):
    """
    This class describes an admin test case.
    """

    def setUp(self):
        self._superuser = User.objects.create_superuser(
            "superuser", "superuser@django-redirects.test", "test"
        )
        self._superuser.save()
        self._client = Client()
        login = self._client.login(username="superuser", password="test")
        assert login
        self._redirect = Redirect.objects.create(
            old_path="/obsolete/page-301/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
        )

    def test_admin_urls(self):
        url = reverse("admin:redirects_redirect_add")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:redirects_redirect_changelist")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:redirects_redirect_change", args=(self._redirect.id,))
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:redirects_redirect_delete", args=(self._redirect.id,))
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_changelist_escapes_html_in_notes(self):
        xss = '<script>alert(1)</script>'
        Redirect.objects.create(
            old_path="/xss-notes/",
            new_path=reverse("redirected-301"),
            notes=xss,
            type_status_code=Redirect.TYPE_301,
        )
        url = reverse("admin:redirects_redirect_changelist")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(xss, response.content.decode())

    def test_admin_changelist_escapes_html_in_old_path(self):
        xss = '<script>alert(1)</script>'
        Redirect.objects.create(
            old_path=f"/xss/{xss}/",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
        )
        url = reverse("admin:redirects_redirect_changelist")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(xss, response.content.decode())

    def test_admin_changelist_escapes_html_in_new_path(self):
        xss = '<script>alert(1)</script>'
        Redirect.objects.create(
            old_path="/xss-new-path/",
            new_path=xss,
            type_status_code=Redirect.TYPE_301,
        )
        url = reverse("admin:redirects_redirect_changelist")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(xss, response.content.decode())

    def test_admin_test_display_unsafe_old_path_renders_span(self):
        redirect = Redirect.objects.create(
            old_path="javascript:alert(1)",
            new_path=reverse("redirected-301"),
            type_status_code=Redirect.TYPE_301,
        )
        url = reverse("admin:redirects_redirect_changelist")
        response = self._client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('href="javascript:', response.content.decode())
