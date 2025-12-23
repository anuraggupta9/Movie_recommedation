# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Streamlit.
It recommends similar movies using cosine similarity and displays posters using the TMDB API.
The application is fully deployed and accessible via a live public URL.

## Live Demo:
https://movie-recommend-22je0149.onrender.com/

Note: Hosted on Render free tier, the first load may take a few seconds if the service is idle.

## How It Works:
- Uses content-based filtering
- Movies are represented as vectors
- Cosine similarity is calculated between movies
- Recommends top 5 similar movies
- Movie posters are fetched dynamically using the TMDB API

## Tech Stack:
- Python
- Streamlit
- Pandas
- Pickle
- TMDB API
- Google Drive (for large pkl files)
- Render (deployment)

## Project Structure:
Movie_recommendation/
├── app.py              # Main Streamlit application

├── requirements.txt    # Project dependencies

├── setup.sh            # Render setup script

├── Procfile            # Start command for deployment

├── .gitignore          # Ignored files (pkl, venv, etc.)

└── README.md           # Project documentation

## Installation (Run Locally):
1. Clone the repository
   - git clone https://github.com/anuraggupta9/Movie_recommendation.git
   - cd Movie_recommendation

2. Create virtual environment
   - python -m venv .venv
   - source .venv/bin/activate   (Linux/Mac)
   - .venv\Scripts\activate      (Windows)

3. Install dependencies
   - pip install -r requirements.txt

4. Run the app
   - streamlit run app.py

## Handling Large Files:
- movies.pkl and similarity.pkl are not stored on GitHub
- Files are downloaded automatically from Google Drive at runtime
- This avoids GitHub file size limits and ensures smooth deployment

## API Key Note:
- TMDB API is used to fetch movie posters
- For production, the API key should be stored as an environment variable

## Features:
- Movie selection dropdown
- Top 5 similar movie recommendations
- Dynamic movie posters
- Error handling for API/network failures
- Cloud deployment with automatic rebuilds

## Future Improvements:
- Add movie ratings and overview
- Improve UI/UX
- Add collaborative filtering
- User authentication
- Cache recommendations

## Author:
- Anurag Kumar
- Integrated Mtech(Btech+Mtech) (Mathematics & Computing)
- IIT (ISM) Dhanbad

## Acknowledgements:
- TMDB for movie data and posters
- Streamlit for the framework
- Render for free cloud deployment
