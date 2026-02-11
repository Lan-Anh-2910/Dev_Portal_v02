import streamlit as st


def render():

    # =========================
    # 1️⃣ Sections cho sidebar phải
    # =========================
    sections = [
        {"label": "Flow", "id": "flow", "level": 2},
        {"label": "URL", "id": "url", "level": 2},
        {"label": "Method", "id": "method", "level": 2},
        {"label": "Request Body", "id": "request-body", "level": 2},
        {"label": "Response", "id": "response", "level": 2},
    ]

    # =========================
    # 2️⃣ Layout trong center (app.py đã chia center/right)
    # =========================
    col_left, col_main = st.columns([1.2, 3])

    # =========================
    # CỘT TRÁI – API ENDPOINTS
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
    # CỘT PHẢI – NỘI DUNG
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

    return sections
