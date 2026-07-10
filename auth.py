import streamlit as st

def initialize_session():#structure for session state variables
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if "username" not in st.session_state:
        st.session_state["username"] = ""
        
    if "role" not in st.session_state:
        st.session_state["role"] = ""
        
        
def is_logged_in():