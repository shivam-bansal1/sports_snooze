import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
from PIL import Image
import requests
import random
import json
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas
import plotly.figure_factory as ff

# df = pd.read_csv('./data/athlete_events.csv')
df = pd.read_csv('./data/athlete_events.zip',compression='zip')
region_df = pd.read_csv('./data/noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Sports Snooze")
st.sidebar.image('./data/img.jpeg')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis','News')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

    st.title("Number of Medals by Countries")
    image = Image.open('Medals_by_countries.png')
    st.image(image, caption='Medals by Country')

if user_menu == 'News':
    st.sidebar.header("News")
    api_key = '07ce6431517e45c5b04b589c36e5bed6'
    url = f"https://newsapi.org/v2/everything?q=olympics&apiKey={api_key}"
    response = requests.get(url)
    response = response.json()
    articles = response['articles']

    def get_news() :
        for article in random.choices(articles) :
            st.header(article['title'])
            st.markdown(f"<span style='background-color:blue; padding:10px; border-radius:20px;'>Published at :{article['publishedAt']}</span>",unsafe_allow_html=True)
            if article['author'] :
                st.write(article['author'])
            st.write(article['source']['name'])
            st.write(article['description'])
            st.image(article['urlToImage'])
        return

    for i in range(5) :
        get_news()

    col1, col2, col3, col4, col5 = st.columns(5)
    if col3.button('Refresh'):
        st.experimental_rerun()

if user_menu == 'Overall Analysis':
    st.sidebar.header("Overall Analysis")

    st.title("Top Statistics")
    editions = df.Year.unique().shape[0]
    cities = df.City.unique().shape[0]
    sports = df.Sport.unique().shape[0]
    events = df.Event.unique().shape[0]
    athletes = df.Name.unique().shape[0]
    nations = df.region.unique().shape[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    st.title("Number of Athletes by Country")
    image = Image.open('Athletes_by_countries.png')
    st.image(image, caption='Athletes by Country' )

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)