from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
from tracker import views  # Import views from the tracker app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the root URL
    path('tracker/', include('tracker.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
