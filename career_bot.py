import streamlit as st
import google.generativeai as genai  # Google Gemini API
import pandas as pd  # Pandas for career Q&A data handling

# ✅ Configure Gemini API
API_KEY = "AIzaSyC1sJ_aHUIsdVumIhkYE5pCTlecWewwhXc"  # Replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Load Career Q&A Data (If Available)
@st.cache_data
def load_career_qa():
    return pd.read_csv("career_q&a.csv")  # Ensure career_qa.csv is in your project

career_qa = load_career_qa()

# ✅ Apply Custom Styling for Background and UI
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #2E86C1;
        text-align: center;
    }
    .stButton button {
        background-color: #2E86C1;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Display Student Image (Use Local Image or URL)
st.image("student.jpg", width=250)  # Ensure "student.jpg" is in your project folder

# ✅ App Title & Description
st.title("🤖 AI Career Guidance")
st.write("Get AI-powered career advice instantly!")

# ✅ User Input
user_input = st.text_input("Enter your career-related question:")

# ✅ Function to Get AI Response
def generate_ai_response(question):
    """Generate response using Google Gemini AI."""
    try:
        response = st.session_state.chat.send_message(question)
        return response.text
    except Exception as e:
        return f"⚠ Error: {str(e)}"

# ✅ Handle User Query
if st.button("Get Answer"):
    if user_input:
        # Use AI to generate career guidance
        ai_response = generate_ai_response(user_input)
        st.write("🤖 AI Response:")
        st.success(ai_response)
    else:
        st.warning("Please enter a question.")

# ✅ Run this script with: streamlit run app.py
