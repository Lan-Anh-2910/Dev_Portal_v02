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
    # CLEAN SIDEBAR STYLE
    # ===============================
    st.sidebar.markdown("""
    <style>
    section[data-testid="stSidebar"] .stRadio > div {
        gap: 0px;
    }

    section[data-testid="stSidebar"] .stRadio label {
        padding: 6px 12px;
        margin: 0px;
        border-left: 3px solid transparent;
        font-size: 14px;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background-color: #f3f4f6;
    }

    section[data-testid="stSidebar"] input[type="radio"] {
        display: none;
    }

    section[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
        border-left: 3px solid #fbbf24;
        background-color: #f9fafb;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### Products")

    with st.sidebar.expander("B2B", expanded=True):

        # ======================
        # MAIN NAV
        # ======================

        main_pages = [
            "overview",
            "integration_methods",
            "sandbox",
            "api_reference",
            "security",
            "sdks",
            "webhook",
            "timeout_handling",
            "common_errors",
        ]

        selected = st.radio(
            "",
            main_pages,
            index=main_pages.index(st.session_state.page)
            if st.session_state.page in main_pages
            else 0,
            format_func=lambda x: x.replace("_", " ").title(),
        )

        st.session_state.page = selected

        st.divider()

        # ======================
        # API v02 TREE
        # ======================

        with st.expander("API Reference v02", expanded=True):

            level1 = st.radio(
                "Type",
                ["direct", "master"],
                horizontal=True,
                key="v02_type_radio",
            )

            level2 = st.radio(
                "Mode",
                ["basic", "h2h"],
                horizontal=True,
                key="v02_mode_radio",
            )

            selected_ep = st.radio(
                "Endpoint",
                ENDPOINTS,
                key="v02_endpoint_radio",
            )

            st.session_state.page = "api_reference_v02"
            st.session_state.v02_type = level1
            st.session_state.v02_mode = level2
            st.session_state.v02_endpoint = selected_ep

    # Other products
    with st.sidebar.expander("Cross-border"):
        st.caption("Coming soon")

    with st.sidebar.expander("Leadgen"):
        st.caption("Coming soon")

    with st.sidebar.expander("Bill"):
        st.caption("Coming soon")
