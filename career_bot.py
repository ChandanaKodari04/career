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

# ✅ Apply Custom Styling for Background Image with Gradient Overlay
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, rgba(30, 144, 255, 0.6), rgba(50, 205, 50, 0.6), rgba(255, 20, 147, 0.6)),
                    url('think.jpg') no-repeat center center fixed;
        background-blend-mode: overlay;
        background-size: cover;
        color: white;
    }
    
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color: #ffffff;
        text-align: center;
    }
    .stButton button {
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

   
