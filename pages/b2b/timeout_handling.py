import streamlit as st

def render():
    sections = [
        {"label": "Recommended timeout", "id": "recommended-timeout"},
        {"label": "Requirement on timeout", "id": "requirement-timeout"},
        {"label": "Idempotency key", "id": "idempotency-key"},
        {"label": "Safe retry APIs", "id": "safe-retry-apis"},
    ]

    st.title("B2B / Timeout handling")

    # ===== Recommended timeout =====
    st.markdown('<a id="recommended-timeout"></a>', unsafe_allow_html=True)
    st.header("Recommended timeout")
    st.write("""
    Merchants should configure appropriate timeout values when calling APIs.

    Recommended timeout:
    - API requests: 10–15 seconds
    - Webhook endpoint: ≤ 5 seconds
    """)

    # ===== Requirement on timeout =====
    st.markdown('<a id="requirement-timeout"></a>', unsafe_allow_html=True)
    st.header("Requirement on timeout")
    st.write("""
    When a timeout occurs, merchants must handle it carefully to avoid
    duplicate or inconsistent transactions.
    
    On timeout:
    - **Do NOT retry blindly**
    - Always call **Get Transaction Status** to verify the final state
    """)

    # ===== Idempotency key =====
    st.markdown('<a id="idempotency-key"></a>', unsafe_allow_html=True)
    st.header("Idempotency key")
    st.write("""
    An idempotency key is required for **Create Payment** APIs.

    It ensures:
    - Duplicate requests are safely handled
    - Only one transaction is created per unique key
    """)

    # ===== Safe retry APIs =====
    st.markdown('<a id="safe-retry-apis"></a>', unsafe_allow_html=True)
    st.header("Safe retry APIs")
    st.write("""
    The following APIs are safe to retry without side effects:
    
    - GET Transaction Status
    - GET Balance
    """)

    return sections
