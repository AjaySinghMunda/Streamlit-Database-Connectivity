import streamlit as st
import pymongo

conn = pymongo.MongoClient(st.secrets["MONGO_URI"])

try:
    conn.admin.command("ping")
    st.success("Connected to MongoDB Atlas")
except Exception as e:
    st.error(e)
