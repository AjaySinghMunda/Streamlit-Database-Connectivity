import streamlit as st
import pymongo

conn = pymongo.MongoClient(
    st.secrets["MONGO_URI"],
    serverSelectionTimeoutMS=5000
)

try:
    conn.admin.command("ping")
    st.success("Connected to MongoDB Atlas")
except Exception as e:
    st.error(e)
