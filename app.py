import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Feeling Detector", page_icon="💬", layout="centered")

st.title("💬 Feeling Detector - Sentiment Analysis App")
st.write("Analyze the sentiment and subjectivity of your sentence or review using **TextBlob**.")

# Input
text = st.text_area("📝 Enter a sentence, comment, or review below:")

if st.button("🔍 Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Sentiment result
        if polarity > 0:
            sentiment = "Positive 😊"
            st.success(f"**Sentiment:** {sentiment}")
        elif polarity < 0:
            sentiment = "Negative 😠"
            st.error(f"**Sentiment:** {sentiment}")
        else:
            sentiment = "Neutral 😐"
            st.info(f"**Sentiment:** {sentiment}")

        # Subjectivity result
        st.markdown(f"**Subjectivity:** {subjectivity} (0 = Very Objective, 1 = Very Subjective)")

        # Visual
        st.subheader("📊 Sentiment Score Visualization")
        fig, ax = plt.subplots()
        ax.barh(["Polarity", "Subjectivity"], [polarity, subjectivity], color=["green", "orange"])
        ax.set_xlim(-1, 1)
        ax.set_xlabel("Score")
        ax.set_title("Sentiment & Subjectivity Analysis")
        st.pyplot(fig)

        # Additional feedback
        st.markdown("---")
        st.markdown("✅ **Analysis Complete!** You can enter another sentence above.")

