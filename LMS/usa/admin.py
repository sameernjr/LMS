from django.contrib import admin

# Register your models here.
from .models import fullsail, oregonstate, coloradostate, saintlouis
admin.site.register(fullsail)
admin.site.register(oregonstate)
admin.site.register(coloradostate)
admin.site.register(saintlouis)