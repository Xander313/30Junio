from django.contrib import admin
from .models import Docente, Cargo

# Register your models here.
admin.site.register(Docente)   
admin.site.register(Cargo)