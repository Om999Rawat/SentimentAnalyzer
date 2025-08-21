import streamlit as st
from textblob import TextBlob
from src.sentiment_analyzer import analyze_sentiment, classify_sentiment
from src.visualization import plot_sentiment_scores, plot_sentence_polarities

st.title("Advanced Sentiment Analysis App")

user_input = st.text_area("Enter your text:")

if user_input:

    polarity, subjectivity = analyze_sentiment(user_input)
    sentiment_class = classify_sentiment(polarity)

    st.write(f"Sentiment: {sentiment_class}")
    st.write(f"Polarity: {polarity}")
    st.write(f"Subjectivity: {subjectivity}")

    plot_sentiment_scores(polarity, subjectivity)

    sentences = [str(s) for s in TextBlob(user_input).sentences]
    if len(sentences) > 1:
        polarities = [s.sentiment.polarity for s in TextBlob(user_input).sentences]
        plot_sentence_polarities(sentences, polarities)
