import matplotlib.pyplot as plt
import streamlit as st

def plot_sentiment_scores(polarity, subjectivity):
   
    fig, ax = plt.subplots()
    ax.bar(['Polarity', 'Subjectivity'], [polarity, subjectivity], color=['green','blue'])
    ax.set_ylim(-1, 1)
    ax.set_title("Sentiment Scores")
    st.pyplot(fig)

def plot_sentence_polarities(sentences, polarities):
  
    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(range(len(sentences)), polarities, color='purple')
    ax.set_xticks(range(len(sentences)))
    ax.set_xticklabels(sentences, rotation=45, ha='right')
    ax.set_ylim(-1, 1)
    ax.set_ylabel("Polarity")
    ax.set_title("Sentence-wise Polarity")
    st.pyplot(fig)
