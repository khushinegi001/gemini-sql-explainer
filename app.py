import streamlit as st
from google import genai

# PUT YOUR SECRET KEY INSIDE THE QUOTES BELOW
API_KEY = "ENTER_YOUR_GEMINI_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)

st.title("📊 Gemini SQL Query Explainer")
st.write("Upload your SQL file, and let Gemini explain it!")

uploaded_file = st.file_uploader("Choose your SQL file", type=["sql", "txt"])

if uploaded_file is not None:
    sql_content = uploaded_file.read().decode("utf-8")
    st.subheader("📝 Your SQL File Content:")
    st.code(sql_content, language="sql")
    
    if st.button("Explain Queries with Gemini"):
        with st.spinner("Analyzing..."):
            try:
                prompt = f"Explain what these SQL queries do step-by-step in simple language:\n\n{sql_content}"
                response = client.models.generate_content(
                    model='gemini-3.8-flash',

                    contents=prompt,
                )
                st.subheader("💡 Gemini's Explanation:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
