import streamlit as st
from components.product_sidebar import render_product_sidebar
from components.section_sidebar import render_section_sidebar
from components.content_renderer import render_content

st.set_page_config(
    page_title="Dev Portal",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "product" not in st.session_state:
    st.session_state.product = "B2B"
if "subproduct" not in st.session_state:
    st.session_state.subproduct = "Virtual Account"
if "sections" not in st.session_state:
    st.session_state.sections = []

# ---------- LAYOUT ----------
left, main, right = st.columns([2.5, 7, 2.5])

with left:
    render_product_sidebar()

with main:
    render_content()

with right:
    render_section_sidebar()
