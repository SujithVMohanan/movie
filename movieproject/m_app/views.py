from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm


# Create your views here.

def home(request):
    movie = Movie.objects.all()

    content = {
        'movies': movie
    }
    return render(request, 'index.html', content)


def details(request, mid):
    movie = Movie.objects.get(id=mid)
    print(movie)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie = Movie(name=name, desc=desc, year=year, img=img, )
        movie.save()
    return render(request, 'add.html', )


def update(request, sid):
    movie = Movie.objects.get(id=sid)
    print(movie)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html',)