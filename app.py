import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="Ultra-Fast AI Assistant", 
    page_icon="⚡", 
    layout="centered"
)

# App Header
st.title("⚡ Ultra-Fast AI Assistant")
st.write("Bijli ki raftaar se poochiye apna sawaal!")

# Sidebar ya Main area mein API Key input secure tarike se
with st.container():
    api_key = st.text_input(
        "Apni Gemini API Key yahan daalein:", 
        type="password",
        help="Google AI Studio se apni free API key yahan paste karein."
    )

if not api_key:
    st.warning("⚠️ Kripya aage badhne ke liye apni Gemini API Key darj karein.")
    st.stop()

# Configure Gemini safely
try:
    genai.configure(api_key=api_key)
    # Using gemini-1.5-flash for lightning-fast speed
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"API Configuration mein error hai: {e}")
    st.stop()

# Chat interface section
st.divider()
user_input = st.text_area("Aap kya janna chahte hain?", placeholder="Yahan apna sawaal likhein...")

if st.button("Poocho 🚀", type="primary"):
    if user_input.strip() == "":
        st.warning("Kripya pehle kuch likhein!")
    else:
        try:
            with st.spinner("⚡ Jawab aa raha hai..."):
                response = model.generate_content(user_input)
                st.success("Jawab:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Jawab laane mein dikkat aayi: {e}")
