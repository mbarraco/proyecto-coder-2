from django.contrib import admin

from mensages.models import Mensaje, Blog, Autor


admin.site.register(Autor)
admin.site.register(Blog)
admin.site.register(Mensaje)