import streamlit as st

def render():

    sections = [
        "Flow",
        "URL",
        "Method",
        "Headers",
        "Parameters",
        "Request Example",
        "Response Example",
        "Error Codes",
    ]

    # =========================
    # Filters (Business Model / Integration)
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        business_model = st.selectbox(
            "Business Model",
            ["Direct Merchant", "Marketplace", "Partner"],
            key="b2b_business_model"
        )

    with col2:
        integration_type = st.selectbox(
            "Integration",
            ["Basic / Pro", "Host to Host (H2H)"],
            key="b2b_integration_type"
        )

    st.divider()

    # =========================
    # LEFT API ENDPOINT MENU
    # =========================
    st.markdown("### API Endpoints")

    endpoints = [
        "Authenticate Merchant",
        "Create Order",
        "Query Order",
        "Webhook",
        "Refund",
        "Cancel",
    ]

    selected_endpoint = st.radio(
        "",
        endpoints,
        index=1,
        key="b2b_selected_endpoint"
    )

    st.divider()

    # =========================
    # MAIN CONTENT
    # =========================
    if selected_endpoint == "Create Order":

        st.markdown("## Create Order API")

        st.markdown("### Flow")
        st.write("Initiate a new order request.")

        st.markdown("### URL")
        st.code("POST /v1/orders/create", language="bash")

        st.markdown("### Method")
        st.markdown("""
- **POST**
- Authorization: Bearer `{API_KEY}`
- Content-Type: application/json
""")

        st.markdown("### Parameters")
        st.markdown("""
- **amount** *(int, required)* – Order amount in cents  
- **currency** *(string, required)* – Currency code (e.g., 'USD')  
""")

        st.markdown("### Request Example")
        st.code("""
{
  "amount": 1000,
  "currency": "USD",
  "customer_id": "123456",
  "callback_url": "https://example.com/callback"
}
""", language="json")

        st.markdown("### Response Example")
        st.code("""
{
  "order_id": "ord_abc123",
  "status": "success",
  "message": "Order created successfully"
}
""", language="json")

        st.markdown("### Error Codes")
        st.markdown("""
| Code | Description |
|------|-------------|
| 4001 | Invalid amount |
| 4002 | Missing currency |
| 4010 | Unauthorized |
""")

    else:
        st.markdown(f"## {selected_endpoint}")
        st.info("Content coming soon...")

    return sections
