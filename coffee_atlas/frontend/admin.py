from django.contrib import admin

from .models import (
    Coffee,
    Country,
    Farmer,
    Place,
    Processing,
    Region,
    Roastery,
    Variety,
)

admin.site.register(Coffee)
admin.site.register(Country)
admin.site.register(Farmer)
admin.site.register(Place)
admin.site.register(Processing)
admin.site.register(Region)
admin.site.register(Roastery)
admin.site.register(Variety)
