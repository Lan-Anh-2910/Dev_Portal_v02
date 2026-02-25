import streamlit as st
from components.product_sidebar import render_product_sidebar
from components.breadcrumb import render_breadcrumb

st.set_page_config(layout="wide")

# default route
if "product" not in st.session_state:
    st.session_state.product = "b2b"

if "page" not in st.session_state:
    st.session_state.page = "overview"

render_product_sidebar()
render_breadcrumb(st.session_state.product, st.session_state.page)

center, right = st.columns([5.0, 1.0])


# ==============================
# ROUTER MAP (thay cho if/elif)
# ==============================

ROUTES = {
    "b2b": {
        "overview": "pages.b2b.overview",
        "integration_methods": "pages.b2b.integration_methods",
        "sandbox": "pages.b2b.sandbox",
        "api_reference": "pages.b2b.api_reference",
        "api_reference_v02": "pages.b2b.api_reference_v02",
        "security": "pages.b2b.security",
        "sdks": "pages.b2b.sdks",
        "webhook": "pages.b2b.webhook",
        "timeout_handling": "pages.b2b.timeout_handling",
        "common_errors": "pages.b2b.common_errors",
    },
    "cb": {
        "overview": "pages.cb.overview",
        "integration_methods": "pages.cb.integration_methods",
        "sandbox": "pages.cb.sandbox",
        "api_reference": "pages.cb.api_reference",
        "security": "pages.cb.security",
        "sdks": "pages.cb.sdks",
        "webhook": "pages.cb.webhook",
        "timeout_handling": "pages.cb.timeout_handling",
        "common_errors": "pages.cb.common_errors",
    }
}


# ==============================
# CENTER CONTENT
# ==============================

with center:
    product = st.session_state.product
    page = st.session_state.page

    module_path = ROUTES.get(product, {}).get(page)

    if module_path:
        module = __import__(module_path, fromlist=["render"])
        sections = module.render()
    else:
        st.error("Page not found")
        sections = []


# ==============================
# RIGHT SECTION NAV
# ==============================

with right:
    from components.section_sidebar import render_section_sidebar
    render_section_sidebar(sections)
