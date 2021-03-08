from django.contrib import admin
from .models import UserModel, VgModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(VgModel)