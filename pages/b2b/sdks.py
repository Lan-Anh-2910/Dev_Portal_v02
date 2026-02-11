import streamlit as st

def render():
    sections = [
        {"label": "Supported languages", "id": "supported-languages"},
        {"label": "SDK installation", "id": "sdk-installation"},
        {"label": "Basic usage", "id": "basic-usage"},
        {"label": "Versioning", "id": "versioning"},
    ]

    st.title("B2B / SDKs")

    # ===== Supported languages =====
    st.markdown('<a id="supported-languages"></a>', unsafe_allow_html=True)
    st.header("Supported languages")
    st.write("""
    The B2B APIs are supported by official SDKs in the following languages:
    - Java
    - PHP
    - Python
    - Node.js

    SDKs are designed to simplify request signing, authentication,
    and response handling.
    """)

    # ===== SDK installation =====
    st.markdown('<a id="sdk-installation"></a>', unsafe_allow_html=True)
    st.header("SDK installation")
    st.write("""
    SDKs can be installed using common package managers.

    Example:
    - Java: Maven / Gradle
    - Node.js: npm / yarn
    - Python: pip
    - PHP: Composer
    """)

    # ===== Basic usage =====
    st.markdown('<a id="basic-usage"></a>', unsafe_allow_html=True)
    st.header("Basic usage")
    st.write("""
    Typical SDK usage includes:
    - Initializing the client with API credentials
    - Creating requests via SDK methods
    - Handling responses and errors

    SDKs abstract low-level HTTP and signature logic.
    """)

    # ===== Versioning =====
    st.markdown('<a id="versioning"></a>', unsafe_allow_html=True)
    st.header("Versioning")
    st.write("""
    SDK versions follow the API versioning strategy.

    Merchants are recommended to:
    - Pin SDK versions in production
    - Review changelogs before upgrading
    """)

    return sections
