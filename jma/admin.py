from django.contrib import admin

from .models import AreaInformationCity
from .models import Earthquake
from .models import EarthquakeDetail


admin.site.register(AreaInformationCity)
admin.site.register(Earthquake)
admin.site.register(EarthquakeDetail)
