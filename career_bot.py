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
       /* position: absolute;
        top: -50%;
        left: 15%;  /* Move text to the left side */
        transform: translateY(-100%);
        font-size: 3rem;
        font-weight: bold;
        color: rgba(255, 255, 255, 0.7);
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4);
        width: 30%;
        text-align: right;
        z-index: -1;*/
        position: absolute;
        top: 20%;
        left: 5%;
        font-size: 3.5rem;
        font-weight: bold;
        color: rgba(255, 255, 255, 0.9);
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
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
    <div class="background-text">Build Your Career Now</div>
    """,
    unsafe_allow_html=True
)

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
