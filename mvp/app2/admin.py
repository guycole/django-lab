from django.contrib import admin

# Register your models here.

from .models import Gamma
from .models import Delta

admin.site.register(Gamma)
admin.site.register(Delta)