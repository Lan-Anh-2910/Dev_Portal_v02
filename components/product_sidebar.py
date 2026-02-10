import streamlit as st

PAGES = [
    ("overview", "Overview"),
    ("integration_methods", "Integration Methods"),
    ("sandbox", "Sandbox"),
    ("api_reference", "API Reference"),
    ("security", "Security"),
    ("sdks", "SDKs"),
    ("webhook", "Webhook"),
    ("timeout_handling", "Timeout handling"),
    ("common_errors", "Common Errors"),
]

def render_product_sidebar():
    with st.sidebar:
        st.subheader("Products")

        with st.expander("B2B", expanded=True):
            for key, label in PAGES:
                if st.button(label, use_container_width=True):
                    st.session_state.product = "b2b"
                    st.session_state.page = key

        with st.expander("Cross-border"):
            st.caption("Coming soon")

        with st.expander("Leadgen"):
            st.caption("Coming soon")

        with st.expander("Bill"):
            st.caption("Coming soon")
