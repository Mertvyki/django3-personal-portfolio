# Generated by Django 4.1.5 on 2023-01-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blog_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(),
        ),
    ]
