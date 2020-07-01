from django.shortcuts import render
from .api_wrapper import SpotifyAPI


def index_view(request):
    
    search_query = request.GET.get('q')
    query_filter = request.GET.get('filter')
    if not query_filter:
        query_filter = 'track'
    spotify_object = SpotifyAPI('2a4194d5a9a24d3abb3d488d3541d014','2fd9edb269ad48c6af32af22a123d4ba')
    items = spotify_object.search(query=str(search_query), operator=None, operator_query=None, search_type=query_filter )
    context = {
    	'count' : count,
        'items': items,
        'q': search_query,
        'filter' : query_filter
    }
    return render(request, 'musify/index.html', context)
# Create your views here.
