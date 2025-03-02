import streamlit as st
import google.generativeai as genai  # Google Gemini API
import pandas as pd  # Pandas for career Q&A data handling

# ✅ Configure Gemini API
API_KEY = ""  # Replace with your actual API key
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

# ✅ Apply Custom Styling with Side Background Text
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, rgba(255, 0, 150, 0.6), rgba(30, 144, 255, 0.6));
        color: white;
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
    top: 20%;
    left: -55%;
    font-size: 3.5rem;
    font-weight: 900; /* Makes text extra bold */
    color: rgba(255, 255, 255, 1); /* Full white text */
    text-shadow: 6px 6px 15px rgba(0, 0, 0, 0.6); /* Stronger shadow for thickness */
    -webkit-text-stroke: 2px rgba(0, 0, 0, 0.7); /* Black outline around text */
    z-index: -1;
    text-align: left;
    width: 40%;

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

# ✅ App Title & Description
st.title("🚀 AI Career Navigator")
st.write("AI just helps you see the best path forward. Keep learning and growing.")

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
