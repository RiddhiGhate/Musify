from django.shortcuts import render
from .api_wrapper import SpotifyAPI
import requests


def index_view(request):
    
    search_query = request.GET.get('q')
    query_filter = request.GET.get('filter')
    if not query_filter:
        query_filter = 'track'
    spotify_object = SpotifyAPI('e8903904826840e2b1423bedb7f1fd85','3d7f7fc0641646d1ba634e0fac660a9c')
    items = spotify_object.search(query={query_filter : search_query}, operator=None, operator_query=None, search_type=query_filter )

    context = {
        'items' : items,
        'q' : search_query,
        'filter' : query_filter
    }
    return render(request, 'musify/index.html', context)
# Create your views here.
