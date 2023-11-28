"""
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('accounts.urls')),
    path('todo/', include('todo_task.urls')),
    path('admin/', admin.site.urls),

    path('__ debug __ /', include(debug_toolbar.urls)),
]

