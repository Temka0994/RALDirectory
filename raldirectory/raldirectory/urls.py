from django.contrib import admin
from django.urls import path, include
from aircraft.views import aircraft_main
from aircrew.views import aircrew_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('aircraft/', include("aircraft.urls")),
    path('aircrafts/', aircraft_main, name='aircraft_main'),
    path('aircrew/', include("aircrew.urls")),
    path('aircrews/', aircrew_main, name='aircrew_main'),
]
