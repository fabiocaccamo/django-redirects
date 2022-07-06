# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("redirects", "0002_add_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="redirect",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created at"
            ),
        ),
        migrations.AddField(
            model_name="redirect",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated at"
            ),
        ),
    ]
