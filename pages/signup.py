import streamlit as st
import pymongo
conn=pymongo.MongoClient(st.secrets["MONGO_URI"])#Set the connection with mongo database and our code
mydb=conn["CAP"]#CAP is the database name
my=mydb["student"]#student is a collection on mongodb
st.title("📝 S i g n U p")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=str(st.text_input("Mobile Number"))
t4=st.text_input("Email Id")
t5=st.date_input("DOB")
b1=st.button("SIGNUP")
if b1:
       my.insert_one({
        "username": t1,
        "email": t4,
        "mobile_number": t3,
        "date_of_birth": str(t5),
        "password": t2
        })
      
       st.success("✅ Sign Up Successfully")
