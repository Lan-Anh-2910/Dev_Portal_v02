import streamlit as st


def render():

    # =========================
    # 1️⃣ Business Model + Integration (giữ lại)
    # =========================
    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        business_model = st.selectbox(
            "Business Model",
            ["Direct Merchant", "Master Merchant"],
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
        {"label": "Request", "id": "request", "level": 2},
        {"label": "Response", "id": "response", "level": 2},
        {"label": "Error Codes", "id": "error-codes", "level": 2}
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

        # ----- Request -----
        st.markdown("<h2 id='request'>Request </h2>", unsafe_allow_html=True)
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

        # ----- Error Codes -----
    st.markdown("<h2 id='error-codes'>Error Codes</h2>", unsafe_allow_html=True)
    st.code(
        """{
      "error_code": "INVALID_SIGNATURE",
      "message": "The provided signature is invalid."
    }
    
    {
      "error_code": "UNAUTHORIZED",
      "message": "API key is missing or incorrect."
    }
    
    {
      "error_code": "INVALID_PARAMS",
      "message": "Required parameters are missing or invalid."
    }
    
    {
      "error_code": "SYSTEM_ERROR",
      "message": "Internal server error. Please try again later."
    }""",
        language="json"
    )

    return sections
