from django.contrib import admin
from .models import Familiar, Residente, Informe, ParteInforme
# Register your models here.
admin.site.register(Familiar)
admin.site.register(Residente)
admin.site.register(Informe)
admin.site.register(ParteInforme)