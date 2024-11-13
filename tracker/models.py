from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    meal_type = models.CharField(max_length=50)  # e.g., Breakfast, Lunch, Dinner
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meal_type} on {self.date}"

class MealEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()  # Number of servings or portion size

    def __str__(self):
        return f"{self.food.name} in {self.meal.meal_type}"

class TrackerLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_entries = models.ManyToManyField(MealEntry)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.user.username} on {self.date}"
