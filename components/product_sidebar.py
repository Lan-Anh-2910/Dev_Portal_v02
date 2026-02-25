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

    # ===============================
    # Custom CSS (PayPal style)
    # ===============================
    st.sidebar.markdown("""
    <style>
    .menu-item {
        padding: 6px 12px;
        font-size: 14px;
        cursor: pointer;
        border-left: 3px solid transparent;
    }

    .menu-item:hover {
        background-color: #f3f4f6;
    }

    .active-item {
        border-left: 3px solid #fbbf24;
        background-color: #f9fafb;
        font-weight: 500;
    }

    .menu-title {
        font-size: 13px;
        font-weight: 600;
        color: #6b7280;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # helper render
    def nav_item(label, page=None, v02_type=None, v02_mode=None, v02_endpoint=None):

        is_active = False

        if page and st.session_state.page == page:
            if page == "api_reference_v02":
                if (
                    st.session_state.get("v02_type") == v02_type
                    and st.session_state.get("v02_mode") == v02_mode
                    and st.session_state.get("v02_endpoint") == v02_endpoint
                ):
                    is_active = True
            else:
                is_active = True

        css_class = "menu-item active-item" if is_active else "menu-item"

        if st.sidebar.markdown(
            f'<div class="{css_class}">{label}</div>',
            unsafe_allow_html=True,
        ):
            if page:
                st.session_state.page = page
            if v02_type:
                st.session_state.v02_type = v02_type
            if v02_mode:
                st.session_state.v02_mode = v02_mode
            if v02_endpoint:
                st.session_state.v02_endpoint = v02_endpoint

    # =========================
    # PRODUCTS
    # =========================

    st.sidebar.markdown("### Products")

    with st.sidebar.expander("B2B", expanded=True):

        nav_item("Overview", page="overview")
        nav_item("Integration Methods", page="integration_methods")
        nav_item("Sandbox", page="sandbox")
        nav_item("API Reference", page="api_reference")

        st.divider()

        # =========================
        # API Reference v02
        # =========================

        with st.expander("API Reference v02", expanded=True):

            # DIRECT MRC
            with st.expander("Direct MRC", expanded=False):

                # Basic / Pro
                with st.expander("Basic / Pro", expanded=False):
                    for ep in ENDPOINTS:
                        nav_item(
                            ep,
                            page="api_reference_v02",
                            v02_type="direct",
                            v02_mode="basic",
                            v02_endpoint=ep,
                        )

                # H2H
                with st.expander("H2H", expanded=False):
                    for ep in ENDPOINTS:
                        nav_item(
                            ep,
                            page="api_reference_v02",
                            v02_type="direct",
                            v02_mode="h2h",
                            v02_endpoint=ep,
                        )

            # MASTER MRC
            with st.expander("Master MRC", expanded=False):

                # Basic / Pro
                with st.expander("Basic / Pro", expanded=False):
                    for ep in ENDPOINTS:
                        nav_item(
                            ep,
                            page="api_reference_v02",
                            v02_type="master",
                            v02_mode="basic",
                            v02_endpoint=ep,
                        )

                # H2H
                with st.expander("H2H", expanded=False):
                    for ep in ENDPOINTS:
                        nav_item(
                            ep,
                            page="api_reference_v02",
                            v02_type="master",
                            v02_mode="h2h",
                            v02_endpoint=ep,
                        )

        st.divider()

        nav_item("Security", page="security")
        nav_item("SDKs", page="sdks")
        nav_item("Webhook", page="webhook")
        nav_item("Timeout handling", page="timeout_handling")
        nav_item("Common Errors", page="common_errors")

    # =========================
    # Other Products
    # =========================

    with st.sidebar.expander("Cross-border"):
        st.caption("Coming soon")

    with st.sidebar.expander("Leadgen"):
        st.caption("Coming soon")

    with st.sidebar.expander("Bill"):
        st.caption("Coming soon")
