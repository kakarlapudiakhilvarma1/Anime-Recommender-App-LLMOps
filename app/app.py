import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide", page_icon="🎬")
load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# --- CSS: Recommendations box styled like Preferences box ---
st.markdown("""
    <style>
    .header {
        background: linear-gradient(90deg, #284174 0%, #5686c5 100%);
        padding: 12px 0 7px 0;
        color: #fff;
        text-align: center;
        border-radius: 0 0 1.2em 1.2em;
        margin-bottom: 0.5em;
        box-shadow: 0 3px 12px 0 #B0C4DE44;
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        z-index: 1000;
    }
    .footer {
        background: linear-gradient(90deg, #284174 0%, #5686c5 100%);
        color: #fff;
        text-align: center;
        padding: 7px 0 3px 0;
        border-radius: 1.2em 1.2em 0 0;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100vw;
        font-size: 1em;
        letter-spacing: .03em;
        box-shadow: 0 -2px 10px 0 #B0C4DE22;
        z-index: 1000;
    }
    .stApp {
        padding-top: 60px;
        padding-bottom: 38px;
    }
    .side-section, .recommend-section {
        background: #fff;
        border: 1.5px solid #e4e8ee;
        border-radius: 1.1em;
        box-shadow: 0 2px 8px #b0c4de15;
        padding: 1.3em 1.1em 1.1em 1.1em;
        margin-top: 0;
    }
    .recommend-heading {
        margin-top: 0;
        margin-bottom: 0.8em;
        font-size: 1.18em;
        font-weight: 700;
        color: #284174;
        letter-spacing: .01em;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(
    '<div class="header"><h2 style="margin-bottom: 0.13em; font-size: 1.7em; font-weight: 800;">Anime Recommender System</h2>'
    '<p style="font-size: 1em; font-weight: 400; letter-spacing: .025em; margin-top: 0;">Personalized Anime Suggestions with AI</p></div>',
    unsafe_allow_html=True
)

# --- 2-column Layout: Input left, Recommendations right ---
left_col, right_col = st.columns([1.2, 2], gap="small")

with left_col:
    st.markdown('<div class="side-section">', unsafe_allow_html=True)
    st.markdown("#### Your Preferences", unsafe_allow_html=True)
    with st.form("anime_form", clear_on_submit=False):
        query = st.text_input(
            "Enter anime preferences",
            value="",
            placeholder="e.g., light hearted anime with school settings",
            key="anime_input"
        )
        recommend_clicked = st.form_submit_button(
            "Recommend", 
            use_container_width=True,
            help="Get personalized anime recommendations"
        )
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="recommend-section">', unsafe_allow_html=True)
    st.markdown('<div class="recommend-heading">Recommendations</div>', unsafe_allow_html=True)
    if recommend_clicked:
        if query:
            with st.spinner("Fetching recommendations for you..."):
                response = pipeline.recommend(query)
            st.write(response)
        else:
            st.warning("Please enter your anime preferences.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Minimal Fixed Footer ---
st.markdown(
    '<div class="footer">Built with ❤️ using Streamlit & AI &nbsp; | &nbsp; &copy; 2025 Anime Recommender</div>',
    unsafe_allow_html=True
)
