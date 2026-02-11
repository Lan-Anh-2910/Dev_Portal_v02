import streamlit as st

ENDPOINTS = [
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

            # ----- Top Pages -----
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

                # ====================================
                # DIRECT MRC
                # ====================================
                with st.expander("Direct MRC", expanded=False):

                    # Basic / Pro
                    with st.expander("Basic / Pro", expanded=False):
                        for ep in ENDPOINTS:
                            if st.button(
                                ep,
                                key=f"direct_basic_{ep}",
                                use_container_width=True,
                            ):
                                st.session_state.page = "api_reference_v02"
                                st.session_state.v02_type = "direct"
                                st.session_state.v02_mode = "basic"
                                st.session_state.v02_endpoint = ep

                    # H2H
                    with st.expander("H2H", expanded=False):
                        for ep in ENDPOINTS:
                            if st.button(
                                ep,
                                key=f"direct_h2h_{ep}",
                                use_container_width=True,
                            ):
                                st.session_state.page = "api_reference_v02"
                                st.session_state.v02_type = "direct"
                                st.session_state.v02_mode = "h2h"
                                st.session_state.v02_endpoint = ep

                # ====================================
                # MASTER MRC
                # ====================================
                with st.expander("Master MRC", expanded=False):

                    # Basic / Pro
                    with st.expander("Basic / Pro", expanded=False):
                        for ep in ENDPOINTS:
                            if st.button(
                                ep,
                                key=f"master_basic_{ep}",
                                use_container_width=True,
                            ):
                                st.session_state.page = "api_reference_v02"
                                st.session_state.v02_type = "master"
                                st.session_state.v02_mode = "basic"
                                st.session_state.v02_endpoint = ep

                    # H2H
                    with st.expander("H2H", expanded=False):
                        for ep in ENDPOINTS:
                            if st.button(
                                ep,
                                key=f"master_h2h_{ep}",
                                use_container_width=True,
                            ):
                                st.session_state.page = "api_reference_v02"
                                st.session_state.v02_type = "master"
                                st.session_state.v02_mode = "h2h"
                                st.session_state.v02_endpoint = ep

            st.divider()

            # ----- Other Sections (GIỮ NGUYÊN) -----
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
        # Other Products
        # =========================
        with st.expander("Cross-border"):
            st.caption("Coming soon")

        with st.expander("Leadgen"):
            st.caption("Coming soon")

        with st.expander("Bill"):
            st.caption("Coming soon")
