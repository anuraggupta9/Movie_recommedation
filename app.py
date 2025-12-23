import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

# ================= GOOGLE DRIVE DOWNLOAD =================

MOVIES_ID = "1ylBnpIdM-OMx1_f4hN6xFfCSc4VyLbpY"
SIMILARITY_ID = "1ma4lY4NEyK9JiLVE3wOSTNGluIGO1SR9"

@st.cache_resource
def download_from_drive(file_id, output):
    if not os.path.exists(output):
        with st.spinner(f"Downloading {output}..."):
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, output, quiet=False)
    return output

download_from_drive(MOVIES_ID, "movies.pkl")
download_from_drive(SIMILARITY_ID, "similarity.pkl")

# ================= LOAD DATA =================

@st.cache_resource
def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies_df, similarity = load_data()

# ================= TMDB POSTER FUNCTION (SAFE) =================

TMDB_API_KEY = "aa1a07fe07105050ecbe47349703953a"

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    except requests.exceptions.RequestException:
        pass

    return "https://via.placeholder.com/500x750?text=Poster+Unavailable"

# ================= RECOMMENDER =================

def recommend(movie):
    movie_index = movies_df[movies_df["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        names.append(movies_df.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

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
