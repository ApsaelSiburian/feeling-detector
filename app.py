import streamlit as st
from textblob import TextBlob

st.title("Feeling Detector")

text = st.text_area("Enter a sentence or review: ")
if st.button("Analyze"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Sentiment: Positive 😊")
    elif polarity <0:
        st.success("Sentiment: Negative 🤬")
    else:
        st.info("Sentiment: Neutral 😁")
