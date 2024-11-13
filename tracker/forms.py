from django import forms
from .models import Food, Meal, MealEntry, TrackerLog

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'carbs', 'protein', 'fat']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_type']

class MealEntryForm(forms.ModelForm):
    class Meta:
        model = MealEntry
        fields = ['meal', 'food', 'quantity']

class TrackerLogForm(forms.ModelForm):
    class Meta:
        model = TrackerLog
        fields = ['meal_entries']  # In a real app, you may also need to select meals or food items dynamically
