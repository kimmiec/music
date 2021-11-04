# from django.shortcuts import render, redirect
# from django.http import JsonResponse
from .models import Artist, Song
# from .forms import ArtistForm, SongForm

# Create your views here.



#GET
# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'music/artist_list.html', {'artists': artists})

# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'music/song_list.html', {'songs': songs})


#SHOW
# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'music/artist_detail.html', {'artist': artist})

# def song_detail(request, pk):
#     song = Song.objects.get(id=pk)
#     return render(request, 'music/song_detail.html', {'song': song})


# CREATE
# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'music/artist_form.html', {'form': form})

# def song_create(request):
#     if request.method == 'POST':
#         form = SongForm(request.POST)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm()
#     return render(request, 'music/song_form.html', {'form': form})

#EDIT - forms function
# def artist_edit(request, pk):
#     artist = Artist.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'music/artist_form.html', {'form': form})

# def song_edit(request, pk):
#     song = Song.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = SongForm(request.POST, instance=song)
#         if form.is_valid():
#             song = form.save()
#         return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm(instance=song)
#     return render(request, 'music/song_form.html', {'form': form})

#DELETE
# def artist_delete(request, pk):
#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')

# def song_delete(request, pk):
#     Song.objects.get(id=pk).delete()
#     return redirect('song_list')


# def artist_list(request):
#     data = {
#         'name': 'Mamamoo',
#         'photo_url': 'https://0.soompi.io/wp-content/uploads/2019/11/05063353/MAMAMOO1.jpeg',
#         'nationality': 'South Korean'
#     }

#     return JsonResponse(data)

# def artist_list(request):
    # artists = Artist.objects.all().values('name', 'nationality', 'photo_url')
    # ^only grab some attributes from our db, else we cant serialize it
    # artists_list = list(artists)
    # ^convert our artists to a list instead of QuerySet
    # return JsonResponse(artists_list, safe=False)
    # ^safe=False is needed if the first parameter isnt a dictionary

    # SERIALIZER FRAMEWORK VIEWS
from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer