import streamlit as st

import pymongo

conn = pymongo.MongoClient(st.secrets["MONGO_URI"])
mydb = conn["CAP"]
my = mydb["student"]

@st.dialog("CHANGE PASSWORD")
def cp():
    t1 = st.text_input("Enter the old password")
    t2 = st.text_input("Enter the new password", type="password")

    if st.button("Change Password"):

        my.update_one(
            {
                "username": st.session_state["username"],
                "password": t1
            },
            {
                "$set": {"password": t2}
            }
        )

        st.session_state["password"] = t2
        st.success("Password Changed Successfully")
        
        
        
        
#Login check
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.balloons()
c1,c2,c3,c4=st.columns(4)
st.title("🐍All the basic python code")
st.success(f"Welcome :{st.session_state['username']}")
if c1.button("Logout",use_container_width=True):
       del st.session_state["username"]
       st.switch_page("main.py")
if c2.button("See Profile",use_container_width=True):
       str1=st.session_state["username"]
       str2=st.session_state["password"]
       res = my.find({
        "username": str1,
        "password": str2
        })

       for i in res:
              st.success(f"Email : {i['email']}")
              st.success(f"Mobile : {i['mobile_number']}")
              st.success(f"DOB : {i['date_of_birth']}")
              st.success(f"Password : {i['password']}")
              
if c3.button("Change Password",use_container_width=True):
       cp()
       
if c4.button("AI Implimentation", use_container_width=True):
         st.write("AI Implimentation is in progress")
