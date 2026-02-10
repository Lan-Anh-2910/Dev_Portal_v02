import streamlit as st

def render_section_sidebar(sections):
    st.markdown("### Sections")

    for sec in sections:
        # Parent
        st.markdown(
            f"- [{sec['label']}](#{sec['anchor']})",
            unsafe_allow_html=True
        )

        # Children
        if "children" in sec:
            for child in sec["children"]:
                st.markdown(
                    f"  - [{child['label']}](#{child['anchor']})",
                    unsafe_allow_html=True
                )
