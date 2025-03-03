import streamlit as st
import google.generativeai as genai  # Google Gemini API
import pandas as pd  # Pandas for career Q&A data handling

#Configure Gemini API
API_KEY = "AIzaSyC1sJ_aHUIsdVumIhkYE5pCTlecWewwhXc"  # Replace with your actual API key
if not API_KEY:
    st.error("⚠ Please provide a valid Google Gemini API key.")
else:
    genai.configure(api_key=API_KEY)

#Initialize Gemini AI Model
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"⚠ Error initializing AI Model: {str(e)}")

#Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

#Load Career Q&A Data (If Available)
@st.cache_data
def load_career_qa():
    try:
        return pd.read_csv("career_q&a.csv")  # Ensure career_q&a.csv exists
    except FileNotFoundError:
        st.warning("⚠ Career Q&A data file not found.")
        return None

career_qa = load_career_qa()

#Function to Get AI Response
def generate_ai_response(question):
    """Generate a career guidance response using Google Gemini AI."""
    try:
        if not API_KEY:
            return "⚠ API Key is missing. Please configure it properly."

        response = st.session_state.chat.send_message(question)
        return response.text  # Extract and return AI response

    except Exception as e:
        st.error(f"⚠ API Request Failed: {str(e)}")  # Display error message
        return "⚠ Sorry, an error occurred while fetching the response."

#Apply Custom Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, rgba(255, 0, 150, 0.6), rgba(30, 144, 255, 0.6));
        color: rgba(255, 255, 255, 0.8);
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
        overflow: hidden;
        padding: 20px;
    }}

    .background-text {{
        
        position: absolute;
        top: 10%;
        left: -55%;
        font-size: 4rem;
        font-weight: bold;
        text-align: left;
        width: 40%;
         transform: translate(-50%, -50%);
    }}
    h1 {{
        position: relative;
        z-index: 10;
    }}

    .stButton button {{
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 1rem;
        position: relative;
        overflow: hidden;
    }}

    .stButton button::after {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.2);
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
    }}

    .stButton button:hover::after {{
        opacity: 1;
    }}
    </style>
    <div class="background-text">"The Best Way to Predict Your Future is to Create It..."</div>
    """,
    unsafe_allow_html=True
)

# App Title & Description
st.title("🤖 AI Career Navigator")
st.write("AI just helps you see the best path forward. Keep learning and growing.")

# User Input
user_input = st.text_input("Enter your career-related question:")

# Handle User Query
if st.button("Get Answer"):
    if user_input:
        # Use AI to generate career guidance
        ai_response = generate_ai_response(user_input)
        st.write("🤖 AI Response:")
        st.success(ai_response)
    else:
        st.warning("⚠ Please enter a question.")
