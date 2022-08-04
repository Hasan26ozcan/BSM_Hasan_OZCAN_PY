from django.http import Http404
from django.shortcuts import get_list_or_404
# http404 olunca hata veriyor bunu try sayesinde yapıyoruz ama daha kolay da yapabiliriz
# onun çin ise yukardaki get_list_or_404 ile ikisini aynı anda yapıyor
from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        "name":"hasan özcan",
        "movies":movies
    }
    return render(request,"movies/list.html",context)

def detail(request,movie_id):

    movie=get_list_or_404(Movie,pk=movie_id)
    context={

    }

    return render(request,"movies/detail.html")
def search(request):
    return render(request,"movies/search.html")
