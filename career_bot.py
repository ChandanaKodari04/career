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

# ✅ Apply Custom Styling with Spacing and Centered Content
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, rgba(255, 0, 150, 0.6), rgba(30, 144, 255, 0.6));
        color: white;
        position: relative;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}

    .background-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 4rem;
        font-weight: bold;
        color: rgba(255, 255, 255, 0.3);
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
        z-index: -1;
        width: 100%;
        text-align: center;
    }}

    .content {{
        position: relative;
        z-index: 10;
        background: rgba(0, 0, 0, 0.2);
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        width: 50%;
        text-align: center;
    }}

    .stTextInput, .stButton {{
        margin-top: 15px;
        margin-bottom: 15px;
    }}

    .stButton button {{
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        padding: 12px;
        font-size: 1.1rem;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
        transition: 0.3s;
    }}

    .stButton button:hover {{
        background-color: #1a5bcc;
    }}
    </style>
    <div class="background-text">Build Your Career Now</div>
    """,
    unsafe_allow_html=True
)

# ✅ Centered Content with Spacing
with st.container():
    st.markdown('<div class="content">', unsafe_allow_html=True)
    
    # ✅ App Title & Description
    st.title("🤖 AI Career Guidance")
    st.write("Get AI-powered career advice instantly!")
    st.markdown("<br>", unsafe_allow_html=True)  # Space below title

    # ✅ User Input
    user_input = st.text_input("Enter your career-related question:")
    st.markdown("<br>", unsafe_allow_html=True)  # Space below input

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
