import streamlit as st

def render_breadcrumb(product, page):
    st.markdown(
        f"**{product.upper()}** / {page.replace('_', ' ').title()}",
        unsafe_allow_html=True
    )
