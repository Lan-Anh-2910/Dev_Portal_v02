import streamlit as st

def render():
    sections = [
        {"label": "Authentication mechanism", "id": "auth"},
        {"label": "Request signing", "id": "signing"},
        {"label": "Webhook verification", "id": "webhook-verify"},
        {"label": "Idempotency", "id": "idempotency"},
    ]

    st.title("B2B / Security")

    st.markdown('<a id="auth"></a>', unsafe_allow_html=True)
    st.header("Authentication mechanism")
    st.write("B2B APIs use API Key and Secret Key for authentication.")

    st.markdown('<a id="signing"></a>', unsafe_allow_html=True)
    st.header("Request signing")
    st.write("All requests must be signed using HMAC SHA256.")

    st.markdown('<a id="webhook-verify"></a>', unsafe_allow_html=True)
    st.header("Webhook verification")
    st.write("Webhook payloads must be verified using shared secret.")

    st.markdown('<a id="idempotency"></a>', unsafe_allow_html=True)
    st.header("Idempotency")
    st.write("Idempotency keys prevent duplicate transaction processing.")

    return sections
