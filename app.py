import streamlit as st
from optimizer import optimize_code
from utils import detect_language, download_link

# Title and Description
st.title("AI-Powered Code Optimization Tool")
st.write("Paste your code below or upload a file to get optimization suggestions.")

# Input Methods
code_snippet = st.text_area("Paste your code here:")
uploaded_file = st.file_uploader("Or upload a code file:", type=["py", "js", "cpp", "java"])

# Load code from file if uploaded
if uploaded_file:
    code_snippet = uploaded_file.read().decode("utf-8")
    st.text_area("Code Preview", code_snippet)

# Analyze Code Button
if st.button("Analyze Code"):
    if not code_snippet.strip():
        st.warning("Please provide code to analyze.")
    else:
        # Detect Language
        language = detect_language(code_snippet)
        st.write(f"Detected Language: {language}")

        # Optimize Code
        st.subheader("Optimization Suggestions")
        suggestions = optimize_code(code_snippet)
        st.write(suggestions)

        # Provide Download Link
        st.markdown(download_link(suggestions, "optimization_suggestions.txt"), unsafe_allow_html=True)
#print("done")