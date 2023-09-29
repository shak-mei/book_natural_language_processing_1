import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob('diary/*.txt'))

analyzer = SentimentIntensityAnalyzer()

score = []

for filepath in filepaths:
	with open(filepath, 'r') as file:
		content = file.read()
	scores = analyzer.polarity_scores(content)
	score.append(scores['compound'])

dates = [name.strip('.txt').strip('diary/') for name in filepaths]

st.title('Diary tone')
st.subheader('Compounded')

figure_m = px.line(x=dates, y=score, labels={'x': 'Dates', 'y': 'Mood'})
st.plotly_chart(figure_m)

