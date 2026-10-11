import random
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Aura & Reflections",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for dreamy aesthetics, gradients, and glassmorphism
st.markdown(
    """
    <style>
        /* Import aesthetic fonts */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:ital,wght@0,400;0,500;1,400&family=Plus+Jakarta+Sans:wght@300;400;500&display=swap');

        /* Hide Streamlit default elements for a clean look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Dreamy moving gradient background */
        .stApp {
            background: linear-gradient(-45deg, #1a1c29, #2c163a, #1f2833, #0f172a);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #f3f4f6;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Center container styling */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 4rem;
        }

        /* Glassmorphism card */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 3rem 2.5rem;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            max-width: 600px;
            width: 100%;
            margin: 0 auto;
            animation: fadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Subtitle / Category tag */
        .tag {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 4px;
            color: #a78bfa;
            margin-bottom: 1.5rem;
            font-weight: 500;
        }

        /* Quote text styling */
        .quote-text {
            font-family: 'Cinzel', serif;
            font-size: 1.5rem;
            font-weight: 400;
            line-height: 1.7;
            color: #f8fafc;
            margin-bottom: 2rem;
            font-style: italic;
        }

        /* Custom styling for Streamlit buttons */
        .stButton>button {
            background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
            color: white;
            border: none;
            border-radius: 50px;
            padding: 0.75rem 2.2rem;
            font-size: 0.95rem;
            font-weight: 500;
            letter-spacing: 1px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
            transition: all 0.3s ease;
            display: block;
            margin: 0 auto;
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(236, 72, 153, 0.6);
            background: linear-gradient(135deg, #7c3aed, #db2777);
        }

        /* Footer watermark */
        .footer-note {
            margin-top: 3rem;
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.3);
            letter-spacing: 2px;
            text-transform: uppercase;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Collection of deep, aesthetic reflections
reflections = [
    (
        "Quiet moments are not empty; they are full of answers you were too"
        " busy to hear."
    ),
    (
        "You are allowed to be a masterpiece and a work in progress at the"
        " exact same time."
    ),
    (
        "Some paths are winding not to delay you, but to show you views you"
        " never knew existed."
    ),
    (
        "Protect your peace fiercely; not everything deserves a reaction, and"
        " not every thought deserves a home."
    ),
    (
        "Growth is often quiet. It happens in the spaces where you choose"
        " grace over reaction."
    ),
    (
        "The universe has spent billions of years crafting stars; do not"
        " forget the magnitude of your own light."
    ),
    (
        "Softness is not weakness. It takes an ocean of strength to remain"
        " gentle in a loud world."
    ),
    (
        "Trust the chapters you haven't read yet. Your story is still being"
        " written beautifully."
    ),
]

# Initialize session state for random quotes
if "current_quote" not in st.session_state:
    st.session_state.current_quote = random.choice(reflections)


# Function to change quote on click
def get_new_quote():
    new_q = random.choice(reflections)
    # Ensure it doesn't pick the exact same one back-to-back if possible
    while new_q == st.session_state.current_quote and len(reflections) > 1:
        new_q = random.choice(reflections)
    st.session_state.current_quote = new_q


# App Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Glass Card Container
st.markdown(
    f"""
    <div class="glass-card">
        <div class="tag">✦ Daily Reflection ✦</div>
        <div class="quote-text">"{st.session_state.current_quote}"</div>
    </div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Interactive button centered
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("✦ Reflect ✦", on_click=get_new_quote):
        pass

# Subtle footer
st.markdown(
    '<div style="text-align: center;"><div class="footer-note">Created'
    " with intention</div></div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
