from django.contrib import admin

from aircraft.models import Subdivision, AircraftModel, Aircraft, AircraftPhoto

admin.site.register(Subdivision)
admin.site.register(AircraftModel)
admin.site.register(Aircraft)
admin.site.register(AircraftPhoto)
