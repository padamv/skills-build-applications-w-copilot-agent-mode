"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)


from django.conf import settings
import os

# API prefix for all endpoints
API_PREFIX = 'api/'

def api_docs(request):
    """
    Returns a simple documentation page with the correct Codespace URL for API usage.
    """
    codespace_name = os.environ.get('CODESPACE_NAME', '[CODESPACE_NAME]')
    base_url = f"https://{codespace_name}-8000.app.github.dev/"
    return HttpResponse(f"""
        <h2>Octofit Tracker API</h2>
        <p>Use the following base URL for API requests in Codespaces:</p>
        <pre>{base_url}api/&lt;component&gt;/</pre>
        <p>Example: <code>{base_url}api/activities/</code></p>
        <p>For local development, use <code>http://localhost:8000/api/&lt;component&gt;/</code></p>
        <p><b>Note:</b> If you see HTTPS certificate warnings, you can safely ignore them in Codespaces.</p>
    """, content_type="text/html")

from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_docs, name='api-docs'),
    path(f'{API_PREFIX}', api_root, name='api-root'),
    path(f'{API_PREFIX}', include(router.urls)),
]
