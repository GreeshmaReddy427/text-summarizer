import streamlit as st
from transformers import pipeline

# Load summarizer (only loads once)
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# UI
st.title("📝 Text Summarizer App")
st.write("Paste any long text below and get a summary instantly!")

text = st.text_area("Enter your text here:", height=300)

# Summary length control
length = st.selectbox("Choose summary length:", ["Short", "Medium", "Long"])

length_map = {
    "Short": (30, 60),
    "Medium": (60, 100),
    "Long": (100, 200),
}

if st.button("Summarize"):
    if len(text.strip()) < 50:
        st.warning("Please enter at least 50 characters of text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=length_map[length][1], min_length=length_map[length][0], do_sample=False)
            st.subheader("📌 Summary")
            st.success(summary[0]['summary_text'])
