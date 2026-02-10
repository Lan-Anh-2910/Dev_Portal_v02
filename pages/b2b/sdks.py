import streamlit as st

def render():
    sections = [
        {"label": "Supported languages", "id": "auth"}
    ]

    st.title("B2B / SDKs")

    st.markdown('<a id="auth"></a>', unsafe_allow_html=True)
    st.header("Supported languages")
    st.write("B2B APIs use API Key and Secret Key for authentication.")

    return sections

