from django.contrib import admin
from .models import Food, Meal, MealEntry, TrackerLog

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(MealEntry)
admin.site.register(TrackerLog)
