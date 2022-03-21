# Generated by Django 3.2.11 on 2022-01-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djangocms_frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Form",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="FormTag",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Form tag",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="Input",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Input",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="MultiSelect",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Select multiple",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="Select",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Select",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="SubmitButton",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
                "verbose_name": "Submit button",
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
    ]
