import streamlit as st


def render():

    sections = []

    st.markdown("# API Reference v02")

    st.divider()

    # =========================
    # DIRECT MRC
    # =========================
    with st.expander("Direct MRC", expanded=True):

        # -------------------------
        # BASIC / PRO
        # -------------------------
        with st.expander("Basic / Pro", expanded=True):

            selected_api = st.radio(
                "Select API",
                [
                    "Authenticate Merchant",
                    "Create Order",
                    "Query Order",
                    "Webhook",
                    "Refund",
                    "Cancel"
                ],
                key="v02_basic_selected"
            )

            st.divider()
            st.markdown(f"## {selected_api}")

            st.write("API description goes here...")

            st.code(
                """POST /v1/example
Authorization: Bearer {API_KEY}
Content-Type: application/json""",
                language="bash"
            )

            sections = [
                {"label": "Overview", "id": "overview", "level": 2},
                {"label": "Request", "id": "request", "level": 2},
                {"label": "Response", "id": "response", "level": 2},
            ]

        # -------------------------
        # H2H
        # -------------------------
        with st.expander("H2H", expanded=False):

            selected_h2h = st.radio(
                "Select H2H API",
                [
                    "Authenticate Merchant (H2H)",
                    "Create Order (H2H)"
                ],
                key="v02_h2h_selected"
            )

            st.divider()
            st.markdown(f"## {selected_h2h}")

            st.write("H2H API description goes here...")

            st.code(
                """POST /h2h/v1/example
Authorization: Bearer {API_KEY}
Content-Type: application/json""",
                language="bash"
            )

    return sections
