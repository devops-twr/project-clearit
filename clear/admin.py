from django.contrib import admin
from .models import Callback
from .models import SyllabusRequest

admin.site.register(Callback)
admin.site.register(SyllabusRequest)