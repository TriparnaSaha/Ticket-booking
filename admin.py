from django.contrib import admin

# Register your models here.
from .models import Destination
admin.site.register(Destination)

from .models import booking
admin.site.register(booking)