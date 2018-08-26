from django.contrib import admin

# Register your models here.

from .models import Alpha
from .models import Beta

admin.site.register(Alpha)
admin.site.register(Beta)