import streamlit as st
import pymongo

# Connect to MongoDB Atlas
client = pymongo.MongoClient(st.secrets["MONGO_URI"])

# Select database
db = client["CollegeAcademicPortal"]

# Collections
users = db["users"]