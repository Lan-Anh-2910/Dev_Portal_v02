import streamlit as st

def render():
    sections = [
        {"label": "Overview", "id": "overview"},
        {"label": "Basic / Pro Integration", "id": "basic-pro"},
        {"label": "Host to Host (H2H)", "id": "h2h"},
    ]

    st.title("B2B / Integration Methods")

    # ===== Overview =====
    st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("""
    B2B Virtual Account supports multiple integration methods
    to fit different business models and transaction volumes.
    """)

    # ===== Basic / Pro =====
    st.markdown('<a id="basic-pro"></a>', unsafe_allow_html=True)
    st.header("Basic / Pro Integration")
    st.write("""
    API-based integration suitable for most merchants.
    """)
    st.markdown("""
    - REST API over HTTPS  
    - Callback for payment notification  
    - Fast onboarding  
    """)

    # ===== H2H =====
    st.markdown('<a id="h2h"></a>', unsafe_allow_html=True)
    st.header("Host to Host (H2H)")
    st.write("""
    Dedicated system-to-system integration for high-volume merchants.
    """)
    st.markdown("""
    - Dedicated connection  
    - Higher throughput  
    - Enhanced security  
    """)

    return sections
