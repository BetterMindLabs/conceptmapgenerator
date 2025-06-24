import streamlit as st
import google.generativeai as genai

# === Gemini Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI ===
st.set_page_config(page_title="🧠 Concept Map Generator")
st.title("🧠 AI-Powered Concept Map Generator")
st.write("Enter any topic and generate a structured concept map in plain text with nodes and links.")

# === Input ===
topic = st.text_input("Enter your topic", placeholder="e.g., Photosynthesis, Pythagorean Theorem, Artificial Intelligence")

if st.button("Generate Concept Map") and topic.strip():
    with st.spinner("Building concept map..."):
        prompt = f"""
You are a teaching assistant model that generates structured concept maps.

Topic: {topic}

Return the concept map with:
- Main concept
- 5–8 key subtopics
- Show connections using arrows (→)
- Use plain text formatting.

Respond like this:
Main: <topic>
<topic> → <sub-concept>
<sub-concept> → <further detail> (optional)
...

Use 7–12 lines max.
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("🧩 Concept Map Structure")
        st.code(result)
