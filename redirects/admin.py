# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
from django.contrib import admin
from django.utils.safestring import mark_safe

if django.VERSION < (2, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _

from redirects.models import Redirect


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    def redirect_display(self, obj):
        html = """
            <span style="line-height: 16px;">
                <span style="display: block; white-space: nowrap; font-weight: normal;">
                    <small>{}</small>
                </span>
                <span style="display: block; white-space: nowrap;">
                    <span style="color: rgba(0, 0, 0, 0.4);">&searr; {}</span> {}
                </span>
            </span>
            """.format(
            obj.old_path, _("(410 Gone)") if obj.new_path == "" else "", obj.new_path
        )
        html = mark_safe(html)
        return html

    redirect_display.short_description = _("Redirect")
    redirect_display.allow_tags = True

    def test_display(self, obj):
        css = """
            font-weight: normal;
            font-size: 20px;
            line-height: 1em;
            display: inline-block;
            padding: 0px 7px 7px 7px;
            """
        if obj.new_path == "" or obj.match == Redirect.MATCH_REGEX:
            css += """
                opacity: 0.2;
                pointer-events: none;
                """
        html = """
            <a href="{}" target="_blank" style="{}">&nearr;</a>
            """.format(
            obj.old_path, css
        )
        html = mark_safe(html)
        return html

    test_display.short_description = _("Test")
    test_display.allow_tags = True

    list_display = (
        "redirect_display",
        "match",
        "type_status_code",
        "priority",
        "counter",
        "status_code",
        "test_display",
        "created_at",
        "updated_at",
    )
    list_display_links = ("redirect_display",)
    list_editable = (
        "match",
        "type_status_code",
        "priority",
    )
    list_filter = (
        "site",
        "match",
        "type_status_code",
        "status_code",
    )
    search_fields = (
        "old_path",
        "new_path",
    )
    save_on_top = True
