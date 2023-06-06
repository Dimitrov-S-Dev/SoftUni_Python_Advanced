def movie_organizer(*args):
    movies = {}
    for movie_name, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie_name)

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), sorted(x[0])))

    output = ""
    for genre, movies in sorted_movies:
        output += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            output += f"* {movie}\n"
    return output
