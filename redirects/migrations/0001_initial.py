# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="Redirect",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "old_path",
                    models.CharField(
                        db_index=True,
                        help_text="This can be either an absolute path or a regex (excluding the domain name). ",
                        max_length=255,
                        verbose_name="Old path",
                    ),
                ),
                (
                    "new_path",
                    models.CharField(
                        blank=True,
                        help_text='This can be either an absolute path, an absolute URL, or a regex. If empty a "410 Gone" response will be returned.',
                        max_length=255,
                        verbose_name="New path",
                    ),
                ),
                (
                    "match",
                    models.CharField(
                        choices=[
                            ("exact", "Exact"),
                            ("prefix", "Prefix"),
                            ("regex", "Regex"),
                        ],
                        db_index=True,
                        default="exact",
                        help_text="The redirect match condition.",
                        max_length=20,
                        verbose_name="Match",
                    ),
                ),
                (
                    "type_status_code",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (301, "301 - Permanent"),
                            (302, "302 - Found"),
                            (303, "303 - See Other"),
                            (307, "307 - Temporary"),
                            (308, "308 - Permanent"),
                        ],
                        db_index=True,
                        default=301,
                        help_text="The redirect http status code.",
                        verbose_name="Type",
                    ),
                ),
                (
                    "counter",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="The redirect requests/responses count.",
                        verbose_name="Counter",
                    ),
                ),
                (
                    "status_code",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        db_index=True,
                        default=None,
                        null=True,
                        verbose_name="Status code",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sites.site",
                        verbose_name="Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Redirect",
                "verbose_name_plural": "Redirects",
                "ordering": ["old_path"],
                "unique_together": {("site", "old_path")},
            },
        ),
    ]
