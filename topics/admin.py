from django.contrib import admin
from .models import Users, Topics, Messages

# Register your models here.
admin.site.register(Users)
admin.site.register(Topics)
admin.site.register(Messages)