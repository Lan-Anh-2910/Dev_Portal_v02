import streamlit as st

ENDPOINTS = [
    ("POST", "Authenticate Merchant"),
    ("POST", "Create Order"),
    ("GET", "Query Order"),
    ("POST", "Webhook"),
    ("POST", "Refund"),
    ("POST", "Cancel"),
]


def method_badge(method):
    colors = {
        "GET": "#0d6efd",
        "POST": "#198754",
        "PUT": "#fd7e14",
        "DELETE": "#dc3545",
    }
    color = colors.get(method, "#6c757d")

    return f"""
    <span style="
        background-color:{color};
        color:white;
        padding:2px 6px;
        border-radius:4px;
        font-size:11px;
        margin-right:6px;
    ">
    {method}
    </span>
    """


def render_product_sidebar():
    with st.sidebar:

        st.subheader("Products")

        # =========================
        # B2B
        # =========================
        with st.expander("B2B", expanded=True):

            # Normal pages
            if st.button("Overview", use_container_width=True):
                st.session_state.page = "overview"

            if st.button("Integration Methods", use_container_width=True):
                st.session_state.page = "integration_methods"

            if st.button("API Reference", use_container_width=True):
                st.session_state.page = "api_reference"

            st.divider()

            # =========================
            # API Reference v02 TREE
            # =========================
            with st.expander("API Reference v02", expanded=True):

                st.markdown("**Direct MRC**")

                # -------- Basic / Pro --------
                with st.expander("Basic / Pro", expanded=True):

                    for method, ep in ENDPOINTS:

                        col1, col2 = st.columns([1, 5])

                        with col1:
                            st.markdown(
                                method_badge(method),
                                unsafe_allow_html=True
                            )

                        with col2:
                            if st.button(ep, key=f"v02_{ep}"):
                                st.session_state.page = "api_reference_v02"
                                st.session_state.v02_mode = "basic"
                                st.session_state.v02_endpoint = ep

                # -------- H2H --------
                if st.button("H2H"):
                    st.session_state.page = "api_reference_v02"
                    st.session_state.v02_mode = "h2h"

        # Other products
        with st.expander("Cross-border"):
            st.caption("Coming soon")

        with st.expander("Leadgen"):
            st.caption("Coming soon")

        with st.expander("Bill"):
            st.caption("Coming soon")
