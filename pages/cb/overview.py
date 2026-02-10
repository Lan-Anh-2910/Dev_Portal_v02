import streamlit as st

def render():
    sections = [
        {"label": "Version", "id": "version"},
        {"label": "Terminology Table", "id": "terminology"},
        {"label": "Description", "id": "description"},
        {"label": "Business Models", "id": "business-models"},
    ]

    st.title("Cross-border / Overview")

    # ===== Version =====
    st.markdown('<a id="version"></a>', unsafe_allow_html=True)
    st.header("Version")
    st.write("""
    This documentation applies to **Cross-border API – Version v1.0**.
    """)

    # ===== Terminology =====
    st.markdown('<a id="terminology"></a>', unsafe_allow_html=True)
    st.header("Terminology Table")

    st.table({
        "Term": [
            "Merchant",
            "Direct Merchant",
            "Master Merchant",
            "Callback / Webhook"
        ],
        "Description": [
            "A business that integrates and uses the payment services",
            "A merchant integrating directly with the VA system",
            "A merchant managing multiple sub-merchants",
            "Server-to-server notification for payment events"
        ]
    })

    # ===== Description =====
    st.markdown('<a id="description"></a>', unsafe_allow_html=True)
    st.header("Description")
    st.write("""
    Virtual Account (VA) allows merchants to receive customer payments
    through unique virtual bank account numbers.
    """)

    # ===== Business Models =====
    st.markdown('<a id="business-models"></a>', unsafe_allow_html=True)
    st.header("Business Models")

    st.subheader("Direct Merchant")
    st.write("""
    The merchant integrates directly with the Virtual Account system
    and manages all payment flows independently.
    """)

    st.subheader("Master Merchant")
    st.write("""
    A primary merchant manages multiple sub-merchants
    under a single integration.
    """)

    return sections
