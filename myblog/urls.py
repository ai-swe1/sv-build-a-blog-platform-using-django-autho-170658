from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Root endpoint serving the homepage
    path('', views.home, name='home'),

    # Admin interface
    path('admin/', admin.site.urls),

    # API endpoints defined in the ``blog`` app
    path('api/', include('blog.urls')),
]
