# Generated by Django 4.0.1 on 2022-02-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
