from django.contrib import admin
from .forms import AircraftAdminForm
from .models import Subdivision, AircraftModel, Aircraft, AircraftPhoto

admin.site.register(Subdivision)
admin.site.register(AircraftModel)
admin.site.register(AircraftPhoto)


class AircraftPhotosInLine(admin.TabularInline):
    model = AircraftPhoto


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    form = AircraftAdminForm
    inlines = [AircraftPhotosInLine]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)