from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Food, Meal, MealEntry, TrackerLog
from django.contrib.auth.decorators import login_required
from .forms import MealForm, FoodForm, TrackerLogForm  # Forms for handling the creation of meal, food, and logs

def home(request):
    return render(request, 'home.html')  # Create a simple home.html template

# Food Views
@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'tracker/food_list.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')  # Redirect to the food list page after saving
    else:
        form = FoodForm()
    return render(request, 'tracker/add_food.html', {'form': form})

# Meal Views
@login_required
def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'tracker/meal_list.html', {'meals': meals})

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')  # Redirect to the meal list page after saving
    else:
        form = MealForm()
    return render(request, 'tracker/add_meal.html', {'form': form})

# Meal Entry Views
@login_required
def add_meal_entry(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    if request.method == 'POST':
        food_id = request.POST.get('food')
        quantity = request.POST.get('quantity')
        food = Food.objects.get(id=food_id)
        meal_entry = MealEntry(meal=meal, food=food, quantity=quantity)
        meal_entry.save()
        return redirect('meal_list')  # Redirect to the meal list after saving
    else:
        foods = Food.objects.all()
    return render(request, 'tracker/add_meal_entry.html', {'meal': meal, 'foods': foods})

# Tracker Log Views
@login_required
def log_food(request):
    if request.method == 'POST':
        form = TrackerLogForm(request.POST)
        if form.is_valid():
            tracker_log = form.save(commit=False)
            tracker_log.user = request.user  # Assign the logged-in user to the tracker log
            tracker_log.save()
            return redirect('tracker_log_list')  # Redirect after saving the log
    else:
        form = TrackerLogForm()
    return render(request, 'tracker/log_food.html', {'form': form})

@login_required
def tracker_log_list(request):
    logs = TrackerLog.objects.filter(user=request.user)
    return render(request, 'tracker/tracker_log_list.html', {'logs': logs})

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signing up
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    
    return render(request, 'tracker/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')  # Redirect to home or any other page
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    
    return render(request, 'tracker/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home or any other page
def goals(request):
    return render(request, 'goals.html')

def schedule_view(request):
    return render(request, 'schedule.html')

def achievements(request):
    return render(request, 'achievements.html') 

def statistics(request):
    return render(request, 'statistics.html') 

def settings(request):
    return render(request, 'settings.html')

def add_goal(request):
   
    return render(request, 'add_goal.html')