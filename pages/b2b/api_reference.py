import streamlit as st

# ===============================
# Page Config
# ===============================
st.set_page_config(layout="wide")

# ===============================
# Header
# ===============================
st.markdown("## B2B / API Reference")

col_filter1, col_filter2 = st.columns(2)

with col_filter1:
    business_model = st.selectbox(
        "Business Model",
        ["Direct Merchant", "Marketplace", "Partner"]
    )

with col_filter2:
    integration_type = st.selectbox(
        "Integration",
        ["Basic / Pro", "Host to Host (H2H)"]
    )

st.divider()

# ===============================
# Main 3-column Layout
# ===============================
col_left, col_main, col_right = st.columns([1, 3, 1])

# =========================================
# LEFT SIDEBAR – API ENDPOINTS
# =========================================
with col_left:
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
        index=1
    )

# =========================================
# MAIN CONTENT
# =========================================
with col_main:

    if selected_endpoint == "Create Order":

        st.markdown("## Create Order API")

        st.markdown("**Flow:** Initiate a new order request.")

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

    else:
        st.markdown(f"## {selected_endpoint}")
        st.info("Content coming soon...")

# =========================================
# RIGHT SIDEBAR – ON THIS PAGE
# =========================================
with col_right:
    st.markdown("### On this page")

    st.markdown("""
- Flow
- URL
- Method
- Headers
- Parameters
- Request Example
- Response Example
- Error Codes
""")
