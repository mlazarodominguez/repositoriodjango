from django.contrib import admin
from .models import Cliente,Reserva,Vuelo,Aeropuerto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Vuelo)
admin.site.register(Aeropuerto)
