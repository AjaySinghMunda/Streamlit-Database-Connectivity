import streamlit as st
import pymongo

conn = pymongo.MongoClient(
    "mongodb+srv://ajay08singhmunda_db_user:PKQROAajnfpfBQOB@cluster0.whgecul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    serverSelectionTimeoutMS=5000
)

try:
    conn.admin.command("ping")
    st.success("Connected to MongoDB Atlas")
except Exception as e:
    st.error(e)
