import streamlit as st
from components.product_sidebar import render_product_sidebar
from components.breadcrumb import render_breadcrumb

# default route
if "product" not in st.session_state:
    st.session_state.product = "b2b"
if "page" not in st.session_state:
    st.session_state.page = "overview"
    
st.set_page_config(layout="wide")

render_product_sidebar()
render_breadcrumb(st.session_state.product, st.session_state.page)

# layout
center, right = st.columns([4.5, 1.5])

with center:
    if st.session_state.product == "b2b":
        page = st.session_state.page

        if page == "overview":
            from pages.b2b.overview import render
        elif page == "integration_methods":
            from pages.b2b.integration_methods import render
        elif page == "sandbox":
            from pages.b2b.sandbox import render
        elif page == "api_reference":
            from pages.b2b.api_reference import render
        elif page == "security":
            from pages.b2b.security import render
        elif page == "sdks":
            from pages.b2b.sdks import render
        elif page == "webhook":
            from pages.b2b.webhook import render
        elif page == "timeout_handling":
            from pages.b2b.timeout_handling import render
        elif page == "common_errors":
            from pages.b2b.common_errors import render

        sections = render()
    if st.session_state.product == "cb":
        page = st.session_state.page

        if page == "overview":
            from pages.cb.overview import render
        elif page == "integration_methods":
            from pages.cb.integration_methods import render
        elif page == "sandbox":
            from pages.cb.sandbox import render
        elif page == "api_reference":
            from pages.cb.api_reference import render
        elif page == "security":
            from pages.cb.security import render
        elif page == "sdks":
            from pages.cb.sdks import render
        elif page == "webhook":
            from pages.cb.webhook import render
        elif page == "timeout_handling":
            from pages.cb.timeout_handling import render
        elif page == "common_errors":
            from pages.cb.common_errors import render
        sections = render()

with right:
    from components.section_sidebar import render_section_sidebar
    render_section_sidebar(sections)
