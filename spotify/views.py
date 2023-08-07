import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db.models.query import QuerySet
from django.forms import forms
from django.shortcuts import render, redirect
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.utils import model_meta
from rest_framework import generics
from .forms import CreatePlaylistForm
from .models import Music, Playlist, Artist, Album
from django.http import HttpResponse, JsonResponse
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.core.serializers.json import DjangoJSONEncoder


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': str(user)
        })


# Serializers define the API representation.
class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        if User.objects.filter(username=request.data['username']).exists():
            return Response("A user with that username already exists.")
        user = User.objects.create_user(
            username=request.data['username'], password=request.data['password'])
        user.save()
        # returns tuple(instance, token)
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'username': user.username
        })
    
    def get_permissions(self, *args, **kwargs):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# Serializers define the API representation.
class MusicSerializer(serializers.HyperlinkedModelSerializer):
    album = AlbumSerializer(read_only=True)
    artist = serializers.StringRelatedField(many=True)
    liked_users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = Music
        fields = ['id', 'url', 'name', 'artist',
                  'album', 'music_path', 'liked_users']


# ViewSets define the view behavior.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        if request.user.id in serializer.data.get('liked_users'):
            data['liked'] = True
        else:
            data['liked'] = False
        return Response(data)

    @action(detail=True, methods=['GET'], name='Like Music')
    def like(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        instance.liked_users.add(request.user.id)
        instance.save()
        data['liked'] = True
        return Response(data)

    @action(detail=True, methods=['GET'], name='Unlike Music')
    def unlike(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        instance.liked_users.remove(request.user.id)
        instance.save()
        data['liked'] = False
        return Response(data)

    @action(detail=False, methods=['GET'], name='userLikedSongs')
    def liked(self, request):
        current_user = request.user
        all_music = current_user.music_set.all()
        serializer = MusicSerializer(
            all_music, many=True, context={'request': request})
        return Response(serializer.data)


# Serializers define the API representation.
class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Playlist
        fields = ['id', 'url', 'name', 'image',
                  'description', 'music', 'created_by']

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                # get function returns None if key doesnt exist
                if self.initial_data.get("remove_music"):
                    instance.music.remove(*value)
                else:
                    instance.music.add(*value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


# ViewSets define the view behavior.
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by'] = request.user
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    @action(detail=False, methods=['GET', 'POST'], name='userLibrary')
    def library(self, request):
        user_playlists = request.user.playlist_set.all()
        if request.data.get('onlyNamesAndId'):
            names = user_playlists.values('name', 'id')
            return Response(names)
        serializer = self.get_serializer(
            user_playlists, many=True, context={'request': request})
        return Response(serializer.data)
