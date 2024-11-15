from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # Your app URLs
    path('foods/', views.food_list, name='food_list'),
    path('foods/add/', views.add_food, name='add_food'),
    path('meals/', views.meal_list, name='meal_list'),
    path('meals/add/', views.add_meal, name='add_meal'),
    path('meals/<int:meal_id>/add-entry/', views.add_meal_entry, name='add_meal_entry'),
    path('log/', views.log_food, name='log_food'),
    path('tracker-logs/', views.tracker_log_list, name='tracker_log_list'),
    path('goals/', views.goals, name='goals'),
    path('goals/add/', views.add_goal, name='add_goal'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('achievements/', views.achievements, name='achievements'),
    path('statistics/', views.statistics, name='statistics'), 
    path('settings/', views.settings, name='settings'),
]
