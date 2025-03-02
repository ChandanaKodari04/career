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

# ✅ Apply Custom Styling for Background Image with Transparent Gradient Overlay
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(to right, rgba(30, 144, 255, 0.5), rgba(50, 205, 50, 0.5), rgba(255, 20, 147, 0.5)),
                    url('think.jpg') no-repeat center center fixed;
        background-size: cover;
        color: white;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        height: 100vh;
        padding-left: 5%;
    }}
    
    .main-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2);
        width: 40%;
        text-align: center;
    }}
    
    h1 {{
        color: white;
        text-align: center;
    }}
    
    .stButton button {{
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        padding: 10px;
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
    """,
    unsafe_allow_html=True
)

# ✅ Display UI on One Side with Image Filling Remaining Space
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ✅ App Title & Description
st.title("🤖 AI Career Guidance")
st.write("Get AI-powered career advice instantly!")

# ✅ User Input with Box
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

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Run this script with: streamlit run app.py
