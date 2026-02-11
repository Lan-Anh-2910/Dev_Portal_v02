import streamlit as st
from components.section_sidebar import render_section_sidebar


def render_api_reference():

    # =========================
    # 1️⃣ Khai báo sections
    # =========================
    sections = [
        {"label": "Flow", "id": "flow", "level": 2},
        {"label": "URL", "id": "url", "level": 2},
        {"label": "Method", "id": "method", "level": 2},
        {"label": "Request Body", "id": "request-body", "level": 2},
        {"label": "Response", "id": "response", "level": 2},
    ]

    # =========================
    # 2️⃣ Layout 3 cột
    # =========================
    col_left, col_main, col_right = st.columns([1.2, 3, 1.2])

    # =========================
    # 3️⃣ CỘT TRÁI – API ENDPOINTS
    # =========================
    with col_left:
        st.markdown("### API Endpoints")

        endpoints = [
            "Authenticate Merchant",
            "Create Order",
            "Query Order",
            "Webhook",
            "Refund",
            "Cancel"
        ]

        for ep in endpoints:
            st.markdown(f"- {ep}")

    # =========================
    # 4️⃣ CỘT PHẢI – SECTIONS
    # =========================
    with col_right:
        render_section_sidebar(sections)

    # =========================
    # 5️⃣ NỘI DUNG CHÍNH
    # =========================
    with col_main:

        st.markdown("# Create Order API")

        # ----- Flow -----
        st.markdown("<h2 id='flow'>Flow</h2>", unsafe_allow_html=True)
        st.write("Initiate a new order request.")

        # ----- URL -----
        st.markdown("<h2 id='url'>URL</h2>", unsafe_allow_html=True)
        st.code("POST /v1/orders/create")

        # ----- Method -----
        st.markdown("<h2 id='method'>Method</h2>", unsafe_allow_html=True)
        st.write("POST")

        # ----- Request Body -----
        st.markdown("<h2 id='request-body'>Request Body</h2>", unsafe_allow_html=True)
        st.code(
            """{
  "merchant_id": "string",
  "amount": 100000,
  "currency": "VND",
  "order_id": "ORDER_001"
}""",
            language="json"
        )

        # ----- Response -----
        st.markdown("<h2 id='response'>Response</h2>", unsafe_allow_html=True)
        st.code(
            """{
  "status": "success",
  "payment_url": "https://..."
}""",
            language="json"
        )
