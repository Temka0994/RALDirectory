from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('aircraft/', include("aircraft.urls")),
    path('aircrew/', include("aircrew.urls")),
]
