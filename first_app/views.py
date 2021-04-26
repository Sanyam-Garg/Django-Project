from django.shortcuts import render
from .models import Musician, Album
from . import forms

from django.db.models import Avg # Built in function to calculate avg of integer data in a table
# Create your views here.

def index(request):
    diction = {
        'title': 'Home Page',
        'musician_list': Musician.objects.order_by('first_name').all() 
    }
    return render(request, 'first_app/index.html', context = diction)

def musician_form(request):
    form = forms.MusicianForm()
    diction = {
        'title': 'Add Musician',
        'musician_form': form,
    } 

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit = True) # Because made using model forms, straight up goes into the database

            return index(request)

    return render(request, 'first_app/musician_form.html', context = diction)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk = artist_id)
    album_list = Album.objects.filter(artist = artist_id)

    artist_rating = Album.objects.filter(artist = artist_id).aggregate(Avg('num_stars'))

    diction = {
        'title': 'Album List',
        'artist': artist_info,
        'album_list': album_list,
        'artist_rating': artist_rating,
    }

    return render(request, 'first_app/album_list.html', context = diction)

def album_form(request):
    form = forms.AlbumForm()
    diction = {
        'title': 'Add Album',
        'album_form': form,
    }  

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return index(request)

    return render(request, 'first_app/album_form.html', context = diction)

def edit_musician(request, artist_id):
    artist = Musician.objects.get(pk = artist_id)
    form = forms.MusicianForm(instance = artist) # This instance actually initializes the value of the respective fields of the form to the ones in the database.
    diction = {
        'title': 'Edit Musician',
        'form': form,
        'artist': artist,
    }  

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance = artist) # This instance is used in the next step to tell django that save(update) the new data in the same row.

        if form.is_valid():
            form.save(commit = True)

            return album_list(request, artist_id)


    return render(request, 'first_app/edit_musician.html', context = diction)

def edit_album(request, album_id):
    album = Album.objects.get(pk = album_id)
    form = forms.AlbumForm(instance = album)
    diction = {
        'title': 'Edit Album',
        'form': form,
        'album': album,
    }

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance = album)

        if form.is_valid():
            form.save(commit = True)

            diction.update({
                'success_text': 'Album updated successfully!',
            })

    return render(request, 'first_app/edit_album.html', context = diction)

def delete_album(request, album_id):
    album = Album.objects.get(pk = album_id).delete()
    diction = {
        'title': 'Delete Page',
        'delete_success': 'Album deleted successfully',
    }    

    return render(request, 'first_app/delete.html', context = diction)

def delete_musician(request, artist_id):
    artist = Musician.objects.get(pk = artist_id).delete()
    diction = {
        'title': 'Delete Musician',
        'delete_success': 'Musician deleted successfully',
    }   

    return render(request, 'first_app/delete.html', context = diction) 