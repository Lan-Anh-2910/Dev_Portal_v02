import streamlit as st

def render_section_sidebar():
    st.markdown("### Sections")

    for section in st.session_state.sections:
        anchor = section.lower().replace(" ", "-")
        st.markdown(f"- [{section}](#{anchor})", unsafe_allow_html=True)
