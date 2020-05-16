from django.shortcuts import render
from django.http import HttpResponse, Http404    
from . models import Movie

# Create your views here.
#MVC


# defining an endpoint
def index(request):
    all_movies = Movie.objects.all() # read Movie table to a list
    return render(request,'index.html', {'title': 'Movies Catalog', 'movies': all_movies})

def details(request, movie_id):
    try:
        the_movie = Movie.objects.get(id=movie_id)
        return render(request, 'details.html', {'test': 'It works!', 'movie' : the_movie} )
    except:
        return render(request, "NotFound.html")
def catalog(request):
    return render(request, 'catalog.html')


def about(request):
    return HttpResponse("Kenneth Judd")



def soon(request):
    return render(request,"comingSoon.html")




