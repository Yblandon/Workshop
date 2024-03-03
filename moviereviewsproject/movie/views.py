from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

# Create your views here.

def home(request):
    searchTerm= request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})


def statistics_view(request):
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()

    genre_counts = {}

    for movie in all_movies:
        if movie.genre.exists():
            primary_genre = movie.genre.first()
            if primary_genre.name in genre_counts:
                genre_counts[primary_genre.name] += 1
            else:
                genre_counts[primary_genre.name] = 1

    # Crear la gráfica de barras
    bar_width = 0.5
    bar_positions = range(len(genre_counts))

    plt.bar(bar_positions, genre_counts.values(), width=bar_width, align='center')
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, genre_counts.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    # Guardar la gráfica en un buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convertir la imagen a base64 para mostrar en la plantilla
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'statistics.html', {'graphic': graphic})


