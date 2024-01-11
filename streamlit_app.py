import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Custom CSS to style the title
st.markdown(""" <style> .font {font-size:50px ; font-family: 'Playfair Display'; color: #FF4242;} </style> """, unsafe_allow_html=True)

# Title
st.markdown('<p class="font"> 🧬DRUG DISCOVERY🧬 </p>', unsafe_allow_html=True)

# Load dataset from GitHub
@st.cache
def load_data():
    # Replace 'raw.githubusercontent.com' with 'raw.github.com' if needed
    url = 'https://raw.githubusercontent.com/aliyashz/DSP/7f847be46f7b0fee9952b39b80d6e102ed1fcb5b/250k_rndm_zinc_drugs.csv'
    data = pd.read_csv(url)
    return data

def home():
    st.title("Home")
    st.write("Welcome to the Home tab!")
    st.write("This is a paragraph of text for the Home tab.")

def about():
    st.title("About")
    st.write("This is the About tab.")
    st.write("Here, you can provide information about your app or project.")

def analysis():
    st.title("Analysis")
    st.write("Explore your data in the Analysis tab.")
    st.write("You can add charts, graphs, and insights here.")

    # Load and display the dataset
    data = load_data()
    st.write("Sample data:")
    st.write(data.head())

def model():
    st.title("Model")
    st.write("Train and deploy your model in the Model tab.")
    st.write("This tab can include information about your machine learning model.")

# Create tabs
tabs = ["Home🏚️", "About❓", "Analysis📊", "Model🤖"]
selected_tab = st.sidebar.selectbox("Select Tab", tabs)

# Display the selected tab content
if selected_tab == "Home🏚️":
    home()
elif selected_tab == "About❓":
    about()
elif selected_tab == "Analysis📊":
    analysis()
elif selected_tab == "Model🤖":
    model()
