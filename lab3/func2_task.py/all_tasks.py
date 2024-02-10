#task1
def above_5_5(movie):
    return movie['imdb'] > 5.5
#task2
def above_5_5_movies(movies):
    return [movie for movie in movies if above_5_5(movie)]

#task3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]
#task4
def average_imdb_score(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)
#task5
def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)