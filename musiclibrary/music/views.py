from django.http.response import Http404
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from PIL import Image

# Create your views here.
class SongList(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SongDetail(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        if song.album_art.name is not None:
            filepath = (f"musiclibrary\media\{song.album_art.name}")
            im = Image.open(filepath)
            im.show()
            print(im.format, im.size, im.mode)
                    
        return Response(serializer.data)

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song) #used to display the song that is deleted below
        song.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)