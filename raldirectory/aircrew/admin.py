from django.contrib import admin

from aircrew.models import Rank, Aircrew, AircraftCrew

admin.site.register(Rank)
admin.site.register(Aircrew)
admin.site.register(AircraftCrew)
