# Generated by Django 3.2.13 on 2024-06-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20240516_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='metadata',
            field=models.JSONField(null=True),
        ),
    ]
