# Generated by Django 3.2.12 on 2022-03-09 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0003_set_site_domain_and_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="site",
            options={
                "ordering": ["domain"],
                "verbose_name": "site",
                "verbose_name_plural": "sites",
            },
        ),
    ]
