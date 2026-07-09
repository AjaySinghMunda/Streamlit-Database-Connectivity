import streamlit as st
import pymongo
import time
with st.spinner("Loading....."):
       time.sleep(1)
conn=pymongo.MongoClient("mongodb+srv://ajay08singhmunda_db_user:PKQROAajnfpfBQOB@cluster0.whgecul.mongodb.net/?appName=Cluster0")
mydb=conn["CAP"]
my=mydb["student"]
st.title("🐍All the basic python code")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("🔑 SIGNIN")
valid=0
if b1:
       ans = my.find({
        "username": t1,
        "password": t2
       })
       for i in ans:
              valid=valid+1
              st.session_state["username"] = i["username"]
              st.session_state["password"]=i['password']
              st.switch_page("pages/profile.py")
                             
       if valid==0:
              st.success("Invalid User Login Details")
