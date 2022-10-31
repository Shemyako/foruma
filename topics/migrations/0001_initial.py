# Generated by Django 4.1.2 on 2022-10-20 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите ник пользователя', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите ник пользователя', max_length=20)),
                ('is_topic', models.BooleanField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.users')),
                ('created_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.topics')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Введите ник пользователя', max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
                ('in_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.topics')),
                ('sended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.users')),
            ],
        ),
    ]
