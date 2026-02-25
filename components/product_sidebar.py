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

    # Sync URL param nếu có
    params = st.query_params
    if "page" in params:
        st.session_state.page = params["page"]

    # ===============================
    # CLEAN SIDEBAR STYLE
    # ===============================
    st.sidebar.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        padding-top: 20px;
    }

    .menu-title {
        font-size: 13px;
        font-weight: 600;
        color: #6b7280;
        margin: 18px 0 8px 0;
    }

    .menu-item {
        padding: 6px 12px;
        font-size: 14px;
        color: #1f2937;
        text-decoration: none;
        display: block;
        border-left: 3px solid transparent;
    }

    .menu-item:hover {
        background-color: #f3f4f6;
    }

    .active {
        border-left: 3px solid #fbbf24;
        background-color: #f9fafb;
        font-weight: 500;
    }

    .submenu {
        margin-left: 15px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### Products")

    # =========================
    # B2B
    # =========================

    st.sidebar.markdown('<div class="menu-title">B2B</div>', unsafe_allow_html=True)

    main_pages = {
        "overview": "Overview",
        "integration_methods": "Integration Methods",
        "sandbox": "Sandbox",
        "api_reference": "API Reference",
        "security": "Security",
        "sdks": "SDKs",
        "webhook": "Webhook",
        "timeout_handling": "Timeout Handling",
        "common_errors": "Common Errors",
    }

    for key, label in main_pages.items():

        active = "active" if st.session_state.page == key else ""

        st.sidebar.markdown(
            f'<a href="?page={key}" class="menu-item {active}">{label}</a>',
            unsafe_allow_html=True
        )

    # =========================
    # API v02
    # =========================

    st.sidebar.markdown('<div class="menu-title">API Reference v02</div>', unsafe_allow_html=True)

    # DIRECT
    st.sidebar.markdown('<div class="submenu"><b>Direct MRC</b></div>', unsafe_allow_html=True)

    st.sidebar.markdown('<div class="submenu submenu"><b>Basic / Pro</b></div>', unsafe_allow_html=True)

    for ep in ENDPOINTS:
        page_key = f"direct_basic_{ep}"
        active = ""

        if (
            st.session_state.page == "api_reference_v02"
            and st.session_state.get("v02_type") == "direct"
            and st.session_state.get("v02_mode") == "basic"
            and st.session_state.get("v02_endpoint") == ep
        ):
            active = "active"

        st.sidebar.markdown(
            f'<a href="?page=api_reference_v02&type=direct&mode=basic&ep={ep}" class="menu-item submenu submenu {active}">{ep}</a>',
            unsafe_allow_html=True
        )

    # Bạn có thể nhân đôi block này cho H2H và Master giống logic trên
