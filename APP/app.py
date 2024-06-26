import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load CSV files
movies = pd.read_csv('APP/movies.csv')

# Display data using Streamlit
st.title('Movie Recommendations')


# Ask user for movie selection from titles from our data set
selected_movie = st.selectbox('Select a movie:', movies['title'])

# Ask user for input to enter number of recommendations
num_recommendations = st.number_input('Enter number of recommendations:', min_value=1, max_value=10, value=5)

# Method for recommendation
cv = TfidfVectorizer()
tfidf_matrix = cv.fit_transform(movies['genres'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movies.index, index=movies['title'])
titles = movies['title']

def recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # Adjusted to return user-specified number of recommendations
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

if st.button('Submit'):
    recommended_movies = recommendations(selected_movie)
    st.subheader('Recommended Movies:')
    st.write(recommended_movies)
