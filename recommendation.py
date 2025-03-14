import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into a format suitable for vectorization
vectorizer = TfidfVectorizer(stop_words="english")
genre_matrix = vectorizer.fit_transform(movies["genres"])

# Compute similarity matrix
similarity = cosine_similarity(genre_matrix)

def recommend_movies(movie_title, num_recommendations=3):
    if movie_title not in movies["title"].values:
        return []

    # Get movie index
    movie_index = movies[movies["title"] == movie_title].index[0]

    # Get similarity scores
    similar_movies = list(enumerate(similarity[movie_index]))
    
    # Sort by similarity score (descending order)
    sorted_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]

    # Return recommended movies
    return [movies.iloc[i[0]]["title"] for i in sorted_movies]
