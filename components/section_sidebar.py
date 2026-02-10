import streamlit as st

def render_section_sidebar(sections):
    st.markdown("### Sections")

    for sec in sections:
        # CHỈ render header cấp cao
        if sec.get("level", 2) == 2:
            st.markdown(
                f"- [{sec['label']}](#{sec['id']})",
                unsafe_allow_html=True
            )
