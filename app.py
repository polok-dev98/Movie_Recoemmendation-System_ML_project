import streamlit as st
import pickle
import pandas as pd
import requests

similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_list)


def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c093744506e9e586653e16675da6a532&language=en-US"
                 .format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:9]
    poster=[]
    recommended_movies=[]

    for i in movie_list:
        movie_ids= movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_ids))
    return recommended_movies,poster


st.title("Movie Recommendation System")

option=st.selectbox(
    "Enter a movie for Recommendation :",
    movies["title"].values
)

if st.button("Recommend"):
    recommendation,post = recommend(option)
    st.header("Hey, you mighth like these 8 movies :")
    col1,col2,col3,col4= st.columns(4)
    col5,col6,col7,col8 = st.columns(4)








    with col1:
        st.text(recommendation[0])
        st.image(post[0])

    with col2:
        st.text(recommendation[1])
        st.image(post[1])

    with col3:
        st.text(recommendation[2])
        st.image(post[2])

    with col4:
        st.text(recommendation[3])
        st.image(post[3])

    with col5:
        st.text(recommendation[4])
        st.image(post[4])

    with col6:
        st.text(recommendation[5])
        st.image(post[5])

    with col7:
        st.text(recommendation[6])
        st.image(post[6])

    with col8:
        st.text(recommendation[7])
        st.image(post[7])
