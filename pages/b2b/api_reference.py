import streamlit as st
from components.section_sidebar import render_section_sidebar


def render():
    center, right = st.columns([4.5, 1.5])

    with center:
        st.title("B2B / API Reference")

        # ===== TAB LEVEL 1 =====
        merchant_tabs = st.tabs(["Direct Merchant", "Master Merchant"])

        with merchant_tabs[0]:
            merchant_type = "Direct Merchant"

        with merchant_tabs[1]:
            merchant_type = "Master Merchant"

        # ===== TAB LEVEL 2 =====
        method_tabs = st.tabs(["Basic / Pro", "H2H"])

        with method_tabs[0]:
            method_type = "Basic / Pro"

        with method_tabs[1]:
            method_type = "H2H"

        st.caption(f"{merchant_type} · {method_type}")

        # ===== API CONTENT =====
        sections = []

        def api_section(title, desc):
            anchor = title.lower().replace(" ", "-")
            st.markdown(f'<a id="{anchor}"></a>', unsafe_allow_html=True)
            st.header(title)
            st.write(desc)
            sections.append({"label": title, "id": anchor})

        api_section(
            "Authenticate Merchant",
            "Authenticate merchant using API Key and Signature."
        )

        api_section(
            "Create Order",
            "Create a new payment order with amount and reference ID."
        )

        api_section(
            "Query Order",
            "Retrieve order status using order ID."
        )

        api_section(
            "Webhook",
            "Receive payment status updates via server-to-server callback."
        )

        api_section(
            "Refund",
            "Refund a successful transaction partially or fully."
        )

        api_section(
            "Cancel",
            "Cancel an unpaid or pending transaction."
        )

