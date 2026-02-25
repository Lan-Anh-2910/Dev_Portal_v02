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

        st.header("Products")
        
        # =========================
        # B2B (Custom Expand)
        # =========================
        
        # init state
        if "b2b_open" not in st.session_state:
            st.session_state.b2b_open = True
        
        # CSS để button nhìn như subheader
        st.markdown("""
        <style>
        /* Ẩn style button mặc định */
        section[data-testid="stSidebar"] button {
            background: none !important;
            border: none !important;
            padding: 4px 0px !important;
            text-align: left !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            box-shadow: none !important;
        }
        
        /* Hover nhẹ */
        section[data-testid="stSidebar"] button:hover {
            background-color: transparent !important;
            color: #2563eb !important;
        }
        
        /* Menu item */
        .menu-item {
            padding: 6px 14px;
            font-size: 14px;
            font-weight: 400;
        }
        
        .menu-item:hover {
            background-color: #f3f4f6;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Toggle button (nhìn như subheader)
        arrow = "▾ " if st.session_state.b2b_open else "▸ "
        if st.button(f"{arrow} B2B", key="b2b_toggle"):
            st.session_state.b2b_open = not st.session_state.b2b_open
        
        # Nội dung bên trong
        if st.session_state.b2b_open:
        
            # tạo 2 cột: cột trái làm khoảng trống
            col_space, col_content = st.columns([0.08, 0.92])
        
            with col_content:
        
                if st.button("Overview", key="overview_btn", use_container_width=True):
                    st.session_state.page = "overview"
        
                if st.button("Integration Methods", key="integration_btn", use_container_width=True):
                    st.session_state.page = "integration_methods"
        
                if st.button("Sandbox", key="sandbox_btn", use_container_width=True):
                    st.session_state.page = "sandbox"
        
                if st.button("API Reference", key="api_ref_btn", use_container_width=True):
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
