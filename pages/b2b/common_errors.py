import streamlit as st

def render():
    sections = [
        {"label": "Error response format", "id": "error-response-format"},
        {"label": "Common error codes", "id": "common-error-codes"},
        {"label": "HTTP status mapping", "id": "http-status-mapping"},
        {"label": "Troubleshooting", "id": "troubleshooting"},
    ]

    st.title("B2B / Common Errors")

    # ===== Error response format =====
    st.markdown('<a id="error-response-format"></a>', unsafe_allow_html=True)
    st.header("Error response format")
    st.write("""
    All API errors follow a consistent response structure.
    """)

    st.code("""
{
  "errorCode": "INVALID_REQUEST",
  "errorMessage": "Invalid request parameters",
  "requestId": "abc-123-xyz"
}
""", language="json")

    # ===== Common error codes =====
    st.markdown('<a id="common-error-codes"></a>', unsafe_allow_html=True)
    st.header("Common error codes")

    st.table({
        "Error Code": [
            "INVALID_REQUEST",
            "UNAUTHORIZED",
            "SIGNATURE_INVALID",
            "RESOURCE_NOT_FOUND",
            "DUPLICATE_REQUEST",
            "INTERNAL_ERROR"
        ],
        "Description": [
            "Request parameters are missing or invalid",
            "Authentication failed or token expired",
            "Request signature is invalid",
            "Requested resource does not exist",
            "Duplicate request detected",
            "Unexpected system error"
        ]
    })

    # ===== HTTP status mapping =====
    st.markdown('<a id="http-status-mapping"></a>', unsafe_allow_html=True)
    st.header("HTTP status mapping")

    st.table({
        "HTTP Status": ["400", "401", "403", "404", "409", "500"],
        "Meaning": [
            "Bad Request",
            "Unauthorized",
            "Forbidden",
            "Not Found",
            "Conflict",
            "Internal Server Error"
        ]
    })

    # ===== Troubleshooting =====
    st.markdown('<a id="troubleshooting"></a>', unsafe_allow_html=True)
    st.header("Troubleshooting")
    st.write("""
    When encountering errors:
    - Verify request parameters and headers
    - Check authentication and signature generation
    - Use requestId when contacting support
    - Retry only APIs marked as safe for retry
    """)

    return sections
