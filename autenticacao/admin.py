from django.contrib import admin
from .models import Pessoa,Cargos

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Cargos)