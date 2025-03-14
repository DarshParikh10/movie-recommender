from flask import Flask, render_template, request, jsonify
from recommendation import recommend_movies

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    movie_title = data.get("movie")
    
    recommendations = recommend_movies(movie_title)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
