import pandas as pd

# Expanded dataset with more movies
data = {
    "movie_id": list(range(1, 41)),  # Movie IDs from 1 to 40
    "title": [
        "Inception", "Interstellar", "The Dark Knight", "Avengers: Endgame", "Titanic",
        "Joker", "The Matrix", "Gladiator", "The Shawshank Redemption", "Forrest Gump",
        "The Godfather", "The Lord of the Rings: The Return of the King", "Star Wars: A New Hope", "Spider-Man: No Way Home",
        "Parasite", "The Lion King", "Finding Nemo", "The Conjuring", "A Quiet Place", "Get Out",
        "Pulp Fiction", "Deadpool", "The Grand Budapest Hotel", "La La Land", "The Social Network",
        "The Wolf of Wall Street", "1917", "Dunkirk", "Coco", "Whiplash",
        "Shutter Island", "Blade Runner 2049", "Gravity", "Logan", "The Revenant",
        "A Star Is Born", "Black Panther", "Bohemian Rhapsody", "The Irishman", "Jumanji: Welcome to the Jungle"
    ],
    "genres": [
        "Sci-Fi|Thriller", "Sci-Fi|Drama", "Action|Crime", "Action|Sci-Fi", "Romance|Drama",
        "Drama|Thriller", "Sci-Fi|Action", "Action|Drama", "Drama|Crime", "Drama|Romance",
        "Crime|Drama", "Fantasy|Adventure", "Sci-Fi|Adventure", "Action|Sci-Fi",
        "Drama|Thriller", "Animation|Drama", "Animation|Adventure", "Horror|Thriller", "Horror|Sci-Fi", "Horror|Thriller",
        "Crime|Drama", "Action|Comedy", "Comedy|Drama", "Romance|Musical", "Biography|Drama",
        "Biography|Comedy", "War|Drama", "War|Action", "Animation|Fantasy", "Drama|Music",
        "Thriller|Mystery", "Sci-Fi|Mystery", "Sci-Fi|Adventure", "Action|Drama", "Adventure|Drama",
        "Romance|Drama", "Action|Sci-Fi", "Biography|Music", "Crime|Drama", "Action|Comedy"
    ],
    "ratings": [
        4.8, 4.7, 4.9, 4.6, 4.7, 4.5, 4.8, 4.6, 4.9, 4.8, 4.9, 4.9, 4.7, 4.6,
        4.8, 4.7, 4.6, 4.5, 4.6, 4.7, 4.9, 4.5, 4.6, 4.5, 4.6, 4.5, 4.6, 4.5, 4.7, 4.8,
        4.7, 4.6, 4.5, 4.7, 4.6, 4.5, 4.6, 4.4, 4.3
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("movies.csv", index=False)

print("✅ movies.csv has been created successfully!")
