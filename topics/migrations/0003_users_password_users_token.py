# Generated by Django 4.1.2 on 2022-10-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_alter_topics_created_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
