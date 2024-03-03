import pandas as pd
import json

# Lee el archivo CSV
df = pd.read_csv('movies_initial.csv')


if 'genre' not in df.columns:
    df['genre'] = ''  # Puedes establecer un valor predeterminado si no tienes información sobre géneros.


# Guarda el DataFrame como JSON
df.to_json('movies.json', orient='records')

with open('movies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break

