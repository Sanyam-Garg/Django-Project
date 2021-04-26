from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('musician-form/', views.musician_form, name = 'musician_form'),
    path('album-form/', views.album_form, name = 'album_form'),
    path('album-list/<int:artist_id>/', views.album_list, name = 'album_list'),
    path('edit-musician/<int:artist_id>/', views.edit_musician, name = 'edit_musician'),
    path('edit-album/<int:album_id>', views.edit_album, name = 'edit_album'),
    path('delete-album/<int:album_id>/', views.delete_album, name = 'delete_album'),
    path('delete-musician/<int:artist_id>/', views.delete_musician, name = 'delete_musician'),
]
