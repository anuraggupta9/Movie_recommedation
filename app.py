import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ================= DOWNLOAD FILES IF NOT PRESENT =================

MOVIES_URL = "https://drive.google.com/uc?id=1ylBnpIdM-OMx1_f4hN6xFfCSc4VyLbpY"
SIMILARITY_URL = "https://drive.google.com/uc?id=1ma4lY4NEyK9JiLVE3wOSTNGluIGO1SR9"

def download_file(url, filename):
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename}..."):
            response = requests.get(url)
            with open(filename, "wb") as f:
                f.write(response.content)

download_file(MOVIES_URL, "movies.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# ================= LOAD DATA =================

movies_df = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ================= TMDB POSTER FUNCTION =================

TMDB_API_KEY = "aa1a07fe07105050ecbe47349703953a"

def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    )
    data = response.json()
    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    return "https://via.placeholder.com/500x750?text=No+Image"

# ================= RECOMMENDER =================

def recommend(movie):
    movie_index = movies_df[movies_df["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# ================= UI =================

st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies_df["title"].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
