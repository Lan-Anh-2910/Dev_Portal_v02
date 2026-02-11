import streamlit as st

def render():
    sections = [
        {"label": "Overview", "id": "overview"},
        {"label": "Security & Signature", "id": "security-signature"},
        {"label": "Success Condition", "id": "success-condition"},
        {"label": "Retry & Timeout", "id": "retry-timeout"},
        {"label": "Common headers", "id": "common-headers"},
    ]

    st.title("B2B / Webhook")

    # ===== Overview =====
    st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("""
    Webhook is a server-to-server callback mechanism used to notify merchants
    about payment events asynchronously.
    
    Merchants must expose an HTTPS endpoint to receive webhook requests.
    """)

    # ===== Security & Signature =====
    st.markdown('<a id="security-signature"></a>', unsafe_allow_html=True)
    st.header("Security & Signature")
    st.write("""
    Each webhook request is signed to ensure authenticity and integrity.

    Merchants should:
    - Validate the signature using the shared secret key
    - Reject requests with invalid signatures
    """)

    # ===== Success Condition =====
    st.markdown('<a id="success-condition"></a>', unsafe_allow_html=True)
    st.header("Success Condition")
    st.write("""
    A webhook delivery is considered successful when:
    - The merchant endpoint returns HTTP 200
    - Response is received within the timeout threshold
    """)

    # ===== Retry & Timeout =====
    st.markdown('<a id="retry-timeout"></a>', unsafe_allow_html=True)
    st.header("Retry & Timeout")
    st.write("""
    If the webhook delivery fails:
    - The system will retry multiple times
    - Retry intervals increase progressively
    - Each request has a fixed timeout limit
    """)

    # ===== Common headers =====
    st.markdown('<a id="common-headers"></a>', unsafe_allow_html=True)
    st.header("Common headers")
    st.write("""
    Common HTTP headers included in webhook requests:
    - Content-Type
    - X-Signature
    - X-Timestamp
    - X-Event-Type
    """)

    return sections
