import streamlit as st

def render_content():
    product = st.session_state.product
    subproduct = st.session_state.subproduct

    st.markdown(f"# {product} / {subproduct}")

    sections = []

    # ---------- OVERVIEW ----------
    st.markdown("## Overview")
    st.write(
        "Virtual Account allows merchants to receive payments via unique virtual accounts."
    )
    sections.append("Overview")

    # ---------- USE CASE ----------
    st.markdown("## Use case")
    sections.append("Use case")

    st.markdown("### Direct Merchant")
    st.write("You integrate directly with our VA system.")
    st.button("Direct Merchant - Basic")
    st.button("Direct Merchant - H2H")

    st.markdown("### Master Merchant")
    st.write("You manage multiple sub-merchants under one master account.")

    # ---------- INTEGRATION METHODS ----------
    st.markdown("## Integration Methods")
    sections.append("Integration Methods")

    st.markdown("### Basic / Pro Method")
    st.write("Simple API integration with API Key authentication.")

    st.markdown("### Host-to-Host (H2H)")
    st.write("Secure server-to-server integration.")

    # ---------- SAVE SECTIONS ----------
    st.session_state.sections = sections
