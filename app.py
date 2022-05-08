import pickle

import streamlit as st
import pandas as pd
import requests



def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
     recommended_movie=[]
     for i in movies_list:
          movie_id=i[0]
          #fetch poster from Api

          recommended_movie.append(movies.iloc[i[0]].title)
     return recommended_movie

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommendor")

selected_movie_name= st.selectbox(
     'Select Movie',
     (movies['title'].values))

if st.button('Recommend'):
     recommendation=recommend(selected_movie_name)
     for i in recommendation:
          st.write(i)




