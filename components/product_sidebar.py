import streamlit as st

BASIC_PRO_ENDPOINTS = [
    "Authenticate Merchant",
    "Create Order",
    "Query Order",
    "Webhook",
    "Refund",
    "Cancel",
]

def render_product_sidebar():
    with st.sidebar:

        st.subheader("Products")

        # =========================
        # B2B
        # =========================
        with st.expander("B2B", expanded=True):

            # Top pages
            if st.button("Overview", use_container_width=True):
                st.session_state.page = "overview"

            if st.button("Integration Methods", use_container_width=True):
                st.session_state.page = "integration_methods"

            if st.button("Sandbox", use_container_width=True):
                st.session_state.page = "sandbox"

            if st.button("API Reference", use_container_width=True):
                st.session_state.page = "api_reference"

            st.divider()

            # =========================
            # API Reference v02
            # =========================
            with st.expander("API Reference v02", expanded=True):

                st.markdown("**Direct MRC**")

                # ---- Basic / Pro
                with st.expander("Basic / Pro", expanded=True):

                    for ep in BASIC_PRO_ENDPOINTS:
                        if st.button(ep, key=f"v02_{ep}", use_container_width=True):
                            st.session_state.page = "api_reference_v02"
                            st.session_state.v02_mode = "basic"
                            st.session_state.v02_endpoint = ep

            st.divider()

            # =========================
            # KEEP ORIGINAL SECTIONS
            # =========================
            if st.button("Security", use_container_width=True):
                st.session_state.page = "security"

            if st.button("SDKs", use_container_width=True):
                st.session_state.page = "sdks"

            if st.button("Webhook", use_container_width=True):
                st.session_state.page = "webhook"

            if st.button("Timeout handling", use_container_width=True):
                st.session_state.page = "timeout_handling"

            if st.button("Common Errors", use_container_width=True):
                st.session_state.page = "common_errors"

        # =========================
        # Other products
        # =========================
        with st.expander("Cross-border"):
            st.caption("Coming soon")

        with st.expander("Leadgen"):
            st.caption("Coming soon")

        with st.expander("Bill"):
            st.caption("Coming soon")
