from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Recommendation)
admin.site.register(Itinerary)
admin.site.register(Restaurant)
admin.site.register(City)