import streamlit as st

def render():
    sections = []

    st.title("B2B / Virtual Account")

    st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("Virtual Account allows merchants to receive payments via unique virtual accounts.")
    sections.append({"id": "overview", "label": "Overview"})

    st.markdown('<a id="use-case"></a>', unsafe_allow_html=True)
    st.header("Use case")
    st.subheader("Direct Merchant")
    st.write("You integrate directly with our VA system.")
    st.subheader("Master Merchant")
    st.write("You manage sub-merchants under your system.")
    sections.append({"id": "use-case", "label": "Use case"})

    return sections
