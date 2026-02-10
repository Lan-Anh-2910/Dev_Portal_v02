import streamlit as st

def render():
    sections = [
        {"label": "Base URL", "id": "base-url"},
        {"label": "Test Credentials", "id": "test-credentials"},
    ]

    st.title("B2B / Sandbox")

    # ===== Base URL =====
    st.markdown('<a id="base-url"></a>', unsafe_allow_html=True)
    st.header("Base URL")
    st.write("Use the following base URL to access the sandbox environment:")
    st.code("https://sandbox-api.example.com")

    # ===== Test Credentials =====
    st.markdown('<a id="test-credentials"></a>', unsafe_allow_html=True)
    st.header("Test Credentials")
    st.write("The following credentials are provided for sandbox testing purposes only.")

    st.table({
        "Credential": [
            "Client ID",
            "API Key",
            "Secret Key",
            "Merchant ID"
        ],
        "Value": [
            "sandbox-client-id",
            "sandbox-api-key",
            "sandbox-secret-key",
            "sandbox-merchant-id"
        ]
    })

    return sections
