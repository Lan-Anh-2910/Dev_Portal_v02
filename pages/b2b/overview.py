import streamlit as st

def render():
    sections = []

    # ===== PAGE TITLE =====
    st.title("B2B / Overview")

    # ===== Version =====
    st.markdown('<a id="version"></a>', unsafe_allow_html=True)
    st.header("Version")
    st.write("""
    This documentation applies to **B2B Virtual Account API – Version v1.0**.  
    All endpoints, request/response formats, and behaviors described here are based on this version.
    """)
    sections.append({"id": "version", "label": "Version"})

    # ===== Terminology Table =====
    st.markdown('<a id="terminology-table"></a>', unsafe_allow_html=True)
    st.header("Terminology Table")

    st.table({
        "Term": [
            "Virtual Account (VA)",
            "Merchant",
            "Direct Merchant",
            "Master Merchant",
            "Callback / Webhook"
        ],
        "Description": [
            "A virtual bank account used to receive payments",
            "A business that integrates and uses the payment services",
            "A merchant integrating directly with the VA system",
            "A merchant managing multiple sub-merchants",
            "Server-to-server notification for payment events"
        ]
    })
    sections.append({"id": "terminology-table", "label": "Terminology Table"})

    # ===== Description =====
    st.markdown('<a id="description"></a>', unsafe_allow_html=True)
    st.header("Description")
    st.write("""
    Virtual Account (VA) is a payment solution that allows merchants to receive
    customer payments through unique virtual bank account numbers.
    
    Each transaction is automatically identified and reconciled based on the VA number,
    enabling efficient payment processing and tracking.
    """)
    sections.append({"id": "description", "label": "Description"})

    # ===== Business Models =====
    st.markdown('<a id="business-models"></a>', unsafe_allow_html=True)
    st.header("Business Models")
    st.write("The B2B Virtual Account product supports the following business models:")
    sections.append({"id": "business-models", "label": "Business Models"})

    # ---- Direct Merchant ----
    st.markdown('<a id="direct-merchant"></a>', unsafe_allow_html=True)
    st.subheader("Direct Merchant")
    st.write("""
    In the Direct Merchant model, the merchant integrates directly with the
    Virtual Account system and manages all payment flows independently.
    
    This model is suitable for merchants who:
    - Have a single business entity
    - Want a simple and straightforward integration
    - Do not manage sub-merchants
    """)
    sections.append({"id": "direct-merchant", "label": "Direct Merchant"})

    # ---- Master Merchant ----
    st.markdown('<a id="master-merchant"></a>', unsafe_allow_html=True)
    st.subheader("Master Merchant")
    st.write("""
    In the Master Merchant model, a primary merchant manages multiple sub-merchants
    under one integration.
    
    This model is suitable for platforms or aggregators who:
    - Operate a marketplace or ecosystem
    - Need to onboard and manage multiple sub-merchants
    - Require centralized reporting and settlement
    """)
    sections.append({"id": "master-merchant", "label": "Master Merchant"})

    return sections
