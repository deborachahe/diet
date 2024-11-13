from django.contrib import admin
from django.urls import path, include
from tracker import views  # Import views from the tracker app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the root URL
    path('tracker/', include('tracker.urls')),
]
