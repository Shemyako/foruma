from django.db import models
from django.urls import reverse

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20, help_text ="Введите ник пользователя", unique = True)
    password = models.CharField(max_length=100, null=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    token = models.CharField(max_length=40, null=True, blank=True)
    browser = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Topics(models.Model):
    name = models.CharField(max_length=20, help_text ="Введите ник пользователя")
    created_by = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True)
    is_topic = models.BooleanField()
    created_in = models.ForeignKey('Topics', on_delete=models.SET_NULL, null=True, blank=True)
    time = models.DateTimeField(auto_now = True)
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('topic', args=[str(self.id)])

    def __str__(self):
        return str(self.id) + "." + self.name


class Messages(models.Model):
    text = models.CharField(max_length=20, help_text ="Введите ник пользователя")
    sended_by = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True)
    in_topic = models.ForeignKey('Topics', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now = True)


