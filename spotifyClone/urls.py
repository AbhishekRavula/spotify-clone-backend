"""spotifyClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from spotify.views import UserViewSet, MusicViewSet, PlaylistViewSet, ArtistViewSet, AlbumViewSet, CustomAuthToken
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from django.conf.urls.static import static
from django.conf import settings
# from rest_framework.authtoken.views import CustomAuthToken


# Routers provide an easy way of automatically determining the URL conf.
# from spotify.views import UserViewSet, MusicViewSet, PlaylistViewSet
#
router = routers.DefaultRouter()
# router.register(r'users/current', CurrentUserView.as_view(), "users-current")
router.register(r'users', UserViewSet)
router.register(r'musics', MusicViewSet)    
router.register(r'playlists', PlaylistViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
# router.register(r'profile', ProfileView)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('spotify/', include('spotify.urls')),
    path('token/', CustomAuthToken.as_view())
]

# urlpatterns = [
#     path('', include('spotify.urls')),
#     path('admin/', admin.site.urls),
# ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
