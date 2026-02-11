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

ENDPOINTS = [
    "Authenticate Merchant",
    "Create Order",
    "Query Order",
    "Webhook",
    "Refund",
    "Cancel"
]


def render_product_sidebar():
    with st.sidebar:
        st.subheader("Products")

        with st.expander("B2B", expanded=True):

            # ===============================
            # NORMAL PAGES
            # ===============================
            for key, label in PAGES:
                if st.button(label, use_container_width=True):
                    st.session_state.product = "b2b"
                    st.session_state.page = key

            st.divider()

            # ===============================
            # API REFERENCE V02 TREE
            # ===============================
            st.markdown("### API Reference v02")

            # State control
            st.session_state.setdefault("v02_open", True)
            st.session_state.setdefault("v02_basic_open", True)
            st.session_state.setdefault("v02_mode", "basic")
            st.session_state.setdefault("v02_endpoint", "Create Order")

            # Root
            if st.button("API Reference v02 ▾", use_container_width=True):
                st.session_state.v02_open = not st.session_state.v02_open
                st.session_state.page = "api_reference_v02"

            if st.session_state.v02_open:

                st.markdown("**Direct MRC**")

                # ================= BASIC / PRO =================
                if st.button("↳ Basic / Pro ▾", use_container_width=True):
                    st.session_state.v02_basic_open = not st.session_state.v02_basic_open
                    st.session_state.v02_mode = "basic"
                    st.session_state.page = "api_reference_v02"

                if st.session_state.v02_basic_open:

                    for ep in ENDPOINTS:
                        if st.button(f"    • {ep}", use_container_width=True):
                            st.session_state.product = "b2b"
                            st.session_state.page = "api_reference_v02"
                            st.session_state.v02_mode = "basic"
                            st.session_state.v02_endpoint = ep

                # ================= H2H =================
                if st.button("↳ H2H", use_container_width=True):
                    st.session_state.product = "b2b"
                    st.session_state.page = "api_reference_v02"
                    st.session_state.v02_mode = "h2h"

        with st.expander("Cross-border"):
            st.caption("Coming soon")

        with st.expander("Leadgen"):
            st.caption("Coming soon")

        with st.expander("Bill"):
            st.caption("Coming soon")
