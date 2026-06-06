import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_civic_image(image):

    prompt = """
    Analyze this civic issue image.

    Return ONLY ONE category:

    Garbage
    Water
    Drainage
    Road
    Street Light
    Other

    Return only the category name.
    """

    response = model.generate_content(
        [prompt, image]
    )

    return response.text.strip()