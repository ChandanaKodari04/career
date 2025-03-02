import streamlit as st
import google.generativeai as genai  # Google Gemini API
import pandas as pd  # Pandas for career Q&A data handling
import base64  # For encoding image to base64

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

# ✅ Function to Convert Image to Base64
def get_base64_image(image_path):
    with open(C:\Users\kodar\OneDrive\Documents, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64_image("question mark.jpg")

# ✅ Apply Custom Styling for Background Image with Gradient Overlay
st.markdown(
    f"""
    <style>
    body {{
        background: url('data:image/jpeg;base64,{bg_image}') no-repeat center center fixed,
                    linear-gradient(to right, rgba(30, 144, 255, 0.6), rgba(50, 205, 50, 0.6), rgba(255, 20, 147, 0.6));
        background-blend-mode: overlay;
        background-size: cover;
        color: white;
    }}
    .main {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2);
    }}
    h1 {{
        color: #ffffff;
        text-align: center;
    }}
    .stButton button {{
        background-color: #2575fc;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }}
    </style>
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
