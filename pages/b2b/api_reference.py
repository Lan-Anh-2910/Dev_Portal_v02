import streamlit as st

def render():
    sections = []

    st.title("API Reference")

    for sec in [
        ("auth", "Authenticate Merchant"),
        ("create", "Create order"),
        ("query", "Query order"),
        ("refund", "Refund"),
        ("cancel", "Cancel"),
        ("errors", "Error Codes"),
    ]:
        st.markdown(f'<a id="{sec[0]}"></a>', unsafe_allow_html=True)
        st.header(sec[1])
        st.code("POST /example/api")
        sections.append({"id": sec[0], "label": sec[1]})

    return sections
