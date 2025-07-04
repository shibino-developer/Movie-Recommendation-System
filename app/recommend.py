import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ─── 1) Locate data directory ──────────────────────────────────────────────────
# BASE_DIR is the root of your project (one level above this file)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# ─── 2) Define file paths ─────────────────────────────────────────────────────
ratings_path = os.path.join(DATA_DIR, 'u.data')
movies_path  = os.path.join(DATA_DIR, 'u.item')

# ─── 3) Load datasets ──────────────────────────────────────────────────────────
ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(ratings_path, sep='\t', names=ratings_cols)

movies = pd.read_csv(
    movies_path,
    sep='|',
    header=None,
    usecols=[0, 1],
    names=['movie_id', 'title'],
    encoding='latin-1'
)

# ─── 4) Merge and pivot ────────────────────────────────────────────────────────
df = pd.merge(ratings, movies, on='movie_id')
pivot = df.pivot_table(index='user_id', columns='title', values='rating').fillna(0)

# ─── 5) Compute cosine similarity matrix ───────────────────────────────────────
sim_matrix = cosine_similarity(pivot.T)
sim_df = pd.DataFrame(sim_matrix, index=pivot.columns, columns=pivot.columns)

# ─── 6) Recommendation function ────────────────────────────────────────────────
def recommend(movie_name, top_n=5):
    if movie_name not in sim_df:
        return ["❌ Movie not found in the dataset."]
    # sort distances descending, skip the first (itself), take next top_n
    top_titles = sim_df[movie_name].sort_values(ascending=False)[1:top_n+1].index.tolist()
    return top_titles

# ─── 7) Sample execution ───────────────────────────────────────────────────────
if __name__ == "__main__":
    sample = "Star Wars (1977)"
    results = recommend(sample)
    print(f"\n📽️ Because you liked: {sample}")
    print("🎯 Top 5 Recommendations:")
    for i, title in enumerate(results, 1):
        print(f"{i}. {title}")
