# import streamlit as st
# import pymongo

# conn = pymongo.MongoClient(st.secrets["MONGO_URI"])

# try:
#     conn.admin.command("ping")
#     st.success("Connected to MongoDB Atlas")
# except Exception as e:
#     st.error(e)



import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="College Academic Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Hide Streamlit Default Menu
# --------------------------------------------------

hide_streamlit_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --------------------------------------------------
# Main Layout
# --------------------------------------------------

left, right = st.columns([1.2, 1])

# --------------------------------------------------
# Left Side
# --------------------------------------------------

with left:

    st.markdown("# 🎓 College Academic Portal")

    st.markdown("### Welcome Back!")

    st.write(
        """
        Manage students, attendance, academics,
        examinations and reports from one place.

        A modern academic management portal for
        administrators, teachers and students.
        """
    )

# --------------------------------------------------
# Right Side
# --------------------------------------------------

with right:

    st.subheader("Login")

    admin_tab, teacher_tab, student_tab = st.tabs(
        ["Admin", "Teacher", "Student"]
    )

    # ---------------------- Admin ----------------------

    with admin_tab:

        admin_username = st.text_input(
            "College ID / Username",
            key="admin_username"
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            key="admin_password"
        )

        remember = st.checkbox("Remember Me", key="admin_remember")

        col1, col2 = st.columns(2)

        with col1:
            st.button("Login", key="admin_login", use_container_width=True)

        with col2:
            st.button("Register", key="admin_register", use_container_width=True)

        st.caption("Forgot Password?")

    # ---------------------- Teacher ----------------------

    with teacher_tab:

        teacher_username = st.text_input(
            "College ID / Username",
            key="teacher_username"
        )

        teacher_password = st.text_input(
            "Password",
            type="password",
            key="teacher_password"
        )

        remember = st.checkbox("Remember Me", key="teacher_remember")

        col1, col2 = st.columns(2)

        with col1:
            st.button("Login", key="teacher_login", use_container_width=True)

        with col2:
            st.button("Register", key="teacher_register", use_container_width=True)

        st.caption("Forgot Password?")

    # ---------------------- Student ----------------------

    with student_tab:

        student_username = st.text_input(
            "College ID / Username",
            key="student_username"
        )

        student_password = st.text_input(
            "Password",
            type="password",
            key="student_password"
        )

        remember = st.checkbox("Remember Me", key="student_remember")

        col1, col2 = st.columns(2)

        with col1:
            st.button("Login", key="student_login", use_container_width=True)

        with col2:
            st.button("Register", key="student_register", use_container_width=True)

        st.caption("Forgot Password?")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption("© 2026 College Academic Portal")