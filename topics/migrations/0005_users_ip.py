# Generated by Django 4.1.2 on 2022-10-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
