import streamlit as st


def render():

    # =========================
    # 1️⃣ Business Model + Integration (giữ lại)
    # =========================
    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        business_model = st.selectbox(
            "Business Model",
            ["Direct Merchant", "Marketplace", "Partner"],
            key="b2b_business_model"
        )

    with col_filter2:
        integration_type = st.selectbox(
            "Integration",
            ["Basic / Pro", "Host to Host (H2H)"],
            key="b2b_integration_type"
        )

    st.divider()

    # =========================
    # 2️⃣ Layout trong center
    # =========================
    col_left, col_main = st.columns([1.2, 3])

    # =========================
    # 3️⃣ API Endpoints – CLICK ĐƯỢC
    # =========================
    endpoints = [
        "Authenticate Merchant",
        "Create Order",
        "Query Order",
        "Webhook",
        "Refund",
        "Cancel"
    ]

    if "b2b_selected_endpoint" not in st.session_state:
        st.session_state.b2b_selected_endpoint = "Create Order"

    with col_left:
        st.markdown("### API Endpoints")

        selected_endpoint = st.radio(
            "",
            endpoints,
            key="b2b_selected_endpoint"
        )

    # =========================
    # 4️⃣ Sections cho sidebar phải
    # =========================
    sections = [
        {"label": "Flow", "id": "flow", "level": 2},
        {"label": "URL", "id": "url", "level": 2},
        {"label": "Method", "id": "method", "level": 2},
        {"label": "Request Body", "id": "request-body", "level": 2},
        {"label": "Response", "id": "response", "level": 2},
    ]

    # =========================
    # 5️⃣ Content chính
    # =========================
    with col_main:

        st.markdown(f"# {selected_endpoint} API")

        # ----- Flow -----
        st.markdown("<h2 id='flow'>Flow</h2>", unsafe_allow_html=True)
        st.write(f"This is the flow description for {selected_endpoint}.")

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
