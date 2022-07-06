# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models

if django.VERSION < (2, 0):
    from django.utils.encoding import force_text as force_str
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.encoding import force_str
    from django.utils.translation import gettext_lazy as _

from redirects.http import (
    HttpResponseGone,
    HttpResponsePermanentRedirect,
    HttpResponseSeeOtherRedirect,
    HttpResponseStrictPermanentRedirect,
    HttpResponseStrictTemporaryRedirect,
    HttpResponseTemporaryRedirect,
)

from six import python_2_unicode_compatible

import re


@python_2_unicode_compatible
class Redirect(models.Model):

    TYPE_301 = 301
    TYPE_302 = 302
    TYPE_303 = 303
    TYPE_307 = 307
    TYPE_308 = 308
    TYPE_CHOICES = (
        (TYPE_301, _("301 - Permanent")),
        (TYPE_302, _("302 - Found")),
        (TYPE_303, _("303 - See Other")),
        (TYPE_307, _("307 - Temporary")),
        (TYPE_308, _("308 - Permanent")),
    )

    TYPE_RESPONSE_CLASS = {
        TYPE_301: HttpResponsePermanentRedirect,
        TYPE_302: HttpResponseTemporaryRedirect,
        TYPE_303: HttpResponseSeeOtherRedirect,
        TYPE_307: HttpResponseStrictTemporaryRedirect,
        TYPE_308: HttpResponseStrictPermanentRedirect,
    }

    MATCH_EXACT = "exact"
    MATCH_PREFIX = "prefix"
    MATCH_REGEX = "regex"
    MATCH_CHOICES = (
        (MATCH_EXACT, _("Exact")),
        (MATCH_PREFIX, _("Prefix")),
        (MATCH_REGEX, _("Regex")),
    )

    site = models.ForeignKey(
        Site, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Site")
    )

    old_path = models.CharField(
        db_index=True,
        max_length=255,
        verbose_name=_("Old path"),
        help_text=_(
            "This can be either an absolute path or a regex (excluding the domain name). "
        ),
    )

    new_path = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("New path"),
        help_text=_(
            "This can be either an absolute path, an absolute URL, or a regex. "
            'If empty a "410 Gone" response will be returned.'
        ),
    )

    match = models.CharField(
        db_index=True,
        max_length=20,
        choices=MATCH_CHOICES,
        default=MATCH_EXACT,
        verbose_name=_("Match"),
        help_text=_("The redirect match condition."),
    )

    type_status_code = models.PositiveSmallIntegerField(
        db_index=True,
        choices=TYPE_CHOICES,
        default=TYPE_301,
        verbose_name=_("Type"),
        help_text=_("The redirect http status code."),
    )

    priority = models.PositiveSmallIntegerField(
        blank=True,
        default=0,
        verbose_name=_("Priority"),
        help_text=_("Higher priority redirects are evaluated first."),
    )

    counter = models.PositiveIntegerField(
        blank=True,
        default=0,
        verbose_name=_("Counter"),
        help_text=_("The redirect requests/responses count."),
    )

    status_code = models.PositiveSmallIntegerField(
        db_index=True,
        blank=True,
        null=True,
        default=None,
        verbose_name=_("Status code"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        verbose_name=_("Created at"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=True,
        verbose_name=_("Updated at"),
    )

    def _get_response_path_with_match_exact(self, path):
        if self.old_path.lower() == path.lower():
            return self.new_path
        return None

    def _get_response_path_with_match_prefix(self, path):
        if path.lower().startswith(self.old_path.lower()):
            return self.new_path
        return None

    def _get_response_path_with_match_regex(self, path):
        try:
            old_path_re = re.compile(self.old_path, re.IGNORECASE)
        except re.error:
            # invalid regex
            return None
        old_path_match = re.match(old_path_re, path)
        if old_path_match:
            new_path_repl = self.new_path.replace("$", "\\")
            return re.sub(old_path_re, new_path_repl, path)
        return None

    def get_response_path(self, path):
        if self.match == Redirect.MATCH_EXACT:
            return self._get_response_path_with_match_exact(path)
        elif self.match == Redirect.MATCH_PREFIX:
            return self._get_response_path_with_match_prefix(path)
        elif self.match == Redirect.MATCH_REGEX:
            return self._get_response_path_with_match_regex(path)
        return None

    def get_response(self, path):
        response_path = self.get_response_path(path)
        if response_path is None:
            return None
        self.counter += 1
        self.save()
        if response_path == "":
            return HttpResponseGone()
        response_class = Redirect.TYPE_RESPONSE_CLASS.get(self.type_status_code)
        return response_class(response_path)

    class Meta:
        app_label = "redirects"
        ordering = ["-priority", "old_path"]
        unique_together = [["site", "old_path"]]
        verbose_name = _("Redirect")
        verbose_name_plural = _("Redirects")

    def __str__(self):
        return force_str(
            "{} {}: {} \n---> {}".format(
                _("Redirect"), self.type_status_code, self.old_path, self.new_path
            )
        )
