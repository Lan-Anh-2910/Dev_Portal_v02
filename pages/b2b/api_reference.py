import streamlit as st

def render():
    st.title("B2B / API Reference")

    st.write("""
    This section provides detailed API references for B2B products.
    APIs are grouped by merchant type and integration method.
    """)

    # ========= DIRECT MERCHANT =========
    with st.expander("Direct Merchant", expanded=True):

        # ----- BASIC / PRO -----
        with st.expander("Basic / Pro Method"):
            render_api_group()

        # ----- H2H -----
        with st.expander("Host-to-Host (H2H)"):
            render_api_group(h2h=True)

    # ========= MASTER MERCHANT =========
    with st.expander("Master Merchant"):

        # ----- BASIC / PRO -----
        with st.expander("Basic / Pro Method"):
            render_api_group()

        # ----- H2H -----
        with st.expander("Host-to-Host (H2H)"):
            render_api_group(h2h=True)

    # ❌ API Reference không dùng Sections sidebar
    return []


def render_api_group(h2h=False):
    apis = [
        "Authenticate Merchant",
        "Create Order",
        "Query Order",
        "Webhook",
        "Refund",
        "Cancel"
    ]

    for api in apis:
        with st.expander(api):
            st.markdown(f"**Endpoint**: `/v1/{api.lower().replace(' ', '-')}`")
            st.markdown("**Method**: POST")
            st.markdown("**Description**:")
            st.write(
                "H2H integration API." if h2h
                else "Standard REST API for merchants."
            )
