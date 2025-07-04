# Movie Recommendation System

A simple Python-based movie recommender using collaborative filtering (cosine similarity) on the MovieLens 100K dataset.  
Built with free, open-source tools: Pandas and scikit-learn. Optionally wrapped in a Streamlit web app.

---

## 🔍 Project Overview

- **Goal:** Given a movie title, suggest the top‑N most similar movies based on user ratings.  
- **Algorithm:** Collaborative filtering via cosine similarity on the user–item ratings matrix.  
- **Dataset:** [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) (100,000 ratings from 943 users on 1,682 movies).

---
## 🚀 Installation

1. **Clone the repo**  
  
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
Create a virtual environment (recommended)


python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Download & place the dataset

Download ml-100k.zip from MovieLens

Extract u.data and u.item into the data/ folder

Usage
1. Command‑line Demo

python app/recommend.py
By default, it recommends 5 movies similar to “Toy Story (1995)”.
To try a different title, edit the sample variable at the bottom of recommend.py.

2. Streamlit Web App (Optional)

streamlit run app/app.py
Open your browser at http://localhost:8501

Type a movie name (e.g., “Star Wars (1977)”) and click Recommend

💡 Customization & Extension
Change top_n in recommend(movie, top_n=…) to return more/fewer suggestions.

Hybrid filtering: incorporate genres or content features into the similarity matrix.

Evaluation: split ratings into train/test, compute RMSE or precision@K.

Deployment: containerize with Docker or deploy to Streamlit Cloud/Heroku.

📜 License
This project is released under the MIT License.
