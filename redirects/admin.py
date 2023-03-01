# flake8: noqa: B950

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from redirects.models import Redirect


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    @admin.display(description=_("Redirect"))
    def redirect_display(self, obj):
        gone = _("(410 Gone)") if obj.new_path == "" else ""
        html = f"""
            <span style="line-height: 16px;">
                <span style="display: block; white-space: nowrap; font-weight: normal;">
                    <small>{obj.old_path}</small>
                </span>
                <span style="display: block; white-space: nowrap;">
                    <span style="color: rgba(0, 0, 0, 0.4);">&searr; {gone}</span> {obj.new_path}
                </span>
            </span>
            """.strip()  # noqa: E501
        html = mark_safe(html)
        return html

    @admin.display(description=_("Test"))
    def test_display(self, obj):
        css = """
            font-weight: normal;
            font-size: 20px;
            line-height: 1em;
            display: inline-block;
            padding: 0px 7px 7px 7px;
            """.strip()
        if obj.new_path == "" or obj.match == Redirect.MATCH_REGEX:
            css += """
                opacity: 0.2;
                pointer-events: none;
                """.strip()
        html = f"""
            <a href="{obj.old_path}" target="_blank" style="{css}">&nearr;</a>
            """.strip()
        html = mark_safe(html)
        return html

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
