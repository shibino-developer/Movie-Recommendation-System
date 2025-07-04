import streamlit as st
from recommend import get_similarity_matrix, recommend
import pandas as pd

# ─── Load data ─────────────────────────────────────
try:
    ratings = pd.read_csv('data/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
    movies = pd.read_csv('data/u.item', sep='|', encoding='latin-1', header=None,
                         names=['movie_id', 'title'], usecols=[0, 1])
    df = pd.merge(ratings, movies, on='movie_id')
    sim_df = get_similarity_matrix(df)
except Exception as e:
    st.error(f"❌ Failed to load data or compute similarity matrix:\n\n{e}")
    st.stop()

# ─── UI Layout ─────────────────────────────────────
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System")
st.markdown("Enter a movie you like, and we'll suggest similar ones based on user ratings.")

# Optional: show available movie titles
with st.expander("📜 Show available movie titles"):
    st.write(movies['title'].sample(30).tolist())

# ─── Input Field ───────────────────────────────────
movie_name = st.text_input("🎥 Movie title (e.g., *Toy Story (1995)*):")

# ─── Output ────────────────────────────────────────
if st.button("🔍 Recommend"):
    if movie_name.strip() == "":
        st.warning("⚠️ Please enter a movie title.")
    else:
        result = recommend(movie_name, sim_df)
        if result[0].startswith("❌"):
            st.error(result[0])
        else:
            st.success(f"🎯 Recommendations for: *{movie_name}*")
            for i, r in enumerate(result, 1):
                st.write(f"{i}. 🎬 {r}")

