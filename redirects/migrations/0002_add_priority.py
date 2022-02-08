# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("redirects", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="redirect",
            options={
                "ordering": ["-priority", "old_path"],
                "verbose_name": "Redirect",
                "verbose_name_plural": "Redirects",
            },
        ),
        migrations.AddField(
            model_name="redirect",
            name="priority",
            field=models.PositiveSmallIntegerField(
                blank=True,
                default=0,
                help_text="Higher priority redirects are evaluated first.",
                verbose_name="Priority",
            ),
        ),
    ]
