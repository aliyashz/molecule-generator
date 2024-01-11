import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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
    st.write("Firstly what is Generative AI? Generative AI is an aspect of AI that uses deep-learning algorithms to generate data identical to training data. The original data can be anything from an image to text to molecular structure data. To recognise patterns in the original data and generate new data that resembles it, generative AI uses neural networks as a component of machine learning.")
    st.write("For our model we have chosen Variational Encoder (VAE) to build a model that generates molecules according to their solubility level, SMILE structure, drug-likeness and surface area.")
    st.write("To understand more about how VAEs work watch the video below:")
    st.video("https://youtu.be/fcvYpzHmhvA?si=hkdVSN-zinCAdPqW")

def about():
    st.title("About")
    st.write("Get to know more about our objectives, goals, and aim.")
    st.markdown("Our Main Goal:")
    st.markdown('''
    To develop a VAE model that is trained on diverse chemical structures to capture a wide range of molecular structure for the creation of a molecular generator.''')

def analysis():
    st.title("Analysis")
    st.write("The analysis below displays the Exploratory Data Analysis (EDA) for this project.")
    st.text("Hint 1: SMILES are a textual representation of a molecule's structure.")
    st.text("Hint 2: logP is a measure of a molecule's hydrophobicity or lipophilicity.")
    st.text("Hint 3: qed is a metric used to assess the drug-likeness of a molecule.")
    st.text("Hint 4: SAS represents the surface area of a molecule that is accessible to the solvent.")

   # Load and display the dataset
    data = load_data()
    st.write("ZINC20 data:")
    st.write(data.head())

    # Histogram for logP
    fig_hist, ax_hist = plt.subplots(figsize=(6, 4))
    # Convert "logP" to numeric, handle NaN values, and plot histogram
    sns.histplot(pd.to_numeric(data["logP"], errors='coerce').dropna(), bins=20, kde=True, color='#D65E3E')
    plt.title("Distribution of logP")
    plt.xlabel("logP")
    plt.ylabel("Frequency")

    # Display the histogram plot in Streamlit
    st.pyplot(fig_hist)

    # Correlation heatmap
    corr_matrix = data.corr()
    fig_heatmap, ax_heatmap = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr_matrix, annot=True, cmap="viridis", linewidths=.5)
    plt.title("Correlation Heatmap")

    # Display the heatmap in Streamlit
    st.pyplot(fig_heatmap)

def model():
    st.title("Model")
    st.write("Step one foot closer to AI-generated drugs.")")
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
