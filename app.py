
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mera AI Assistant", page_icon="⚡", layout="centered")

st.title("⚡ Ultra-Fast AI Assistant")
st.write("Bijli ki raftaar se poochiye apna sawaal!")

API_KEY = st.text_input("Apni Gemini API Key yahan daalein:", type="password")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    user_input = st.text_input("Aap kya janna chahte hain?")

    if st.button("Poocho 🚀") and user_input:
        with st.spinner("Jawab aa raha hai..."):
            response = model.generate_content(user_input)
            st.success("Jawab:")
            st.write(response.text)
else:
    st.info("Kripya pehle apni Gemini API Key darj karein taaki assistant active ho sake.")
