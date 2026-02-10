import streamlit as st

PRODUCT_TREE = {
    "B2B": [
        "Virtual Account",
        "BNPL",
        "Installment",
        "Card Payment",
    ],
    "Bill": [],
    "Leadgen": [],
    "Cross-border": [
        "Collection",
        "Disbursement",
        "Check transaction status",
        "Check balance",
        "Payment",
        "Refund",
        "Settlement",
        "Onboarding",
    ],
}

def render_product_sidebar():
    st.markdown("### Products")

    for product, subproducts in PRODUCT_TREE.items():
        with st.expander(product, expanded=(product == st.session_state.product)):
            if not subproducts:
                if st.button(product, key=f"product-{product}"):
                    st.session_state.product = product
                    st.session_state.subproduct = None
            else:
                for sp in subproducts:
                    selected = (
                        product == st.session_state.product
                        and sp == st.session_state.subproduct
                    )

                    label = f"👉 {sp}" if selected else sp

                    if st.button(label, key=f"{product}-{sp}"):
                        st.session_state.product = product
                        st.session_state.subproduct = sp
