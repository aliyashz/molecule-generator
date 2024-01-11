import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load ZINC dataset
csv_path = st.cache_data(pd.read_csv)(
    "https://raw.githubusercontent.com/aliyashz/DSP/7f847be46f7b0fee9952b39b80d6e102ed1fcb5b/250k_rndm_zinc_drugs.csv"
)

# Custom CSS to style the title
st.markdown(""" <style> .font {font-size:50px ; font-family: 'Playfair Display'; color: #FF4242;} </style> """, unsafe_allow_html=True)

# Title
st.markdown('<p class="font"> 🧬DRUG DISCOVERY🧬 </p>', unsafe_allow_html=True)

menu = ["Home 🏚️", "About❓", "Analysis 📊", "Model 🤖"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.write("Step one foot closer to AI-generated drugs.")

elif choice == "About":
    st.write("Get to know more about our objectives, goals, and aim.")

elif choice == "Analysis":
    st.write("The analysis below displays the Exploratory Data Analysis (EDA) for this project.")
    st.write("Hint 1: SMILES are a textual representation of a molecule's structure.")
    st.write("Hint 2: logP is a measure of a molecule's hydrophobicity or lipophilicity.")
    st.write("Hint 3: qed is a metric used to assess the drug-likeness of a molecule.")
    st.write("Hint 4: SAS represents the surface area of a molecule that is accessible to the solvent.")

    # Display the ZINC dataset
    st.write(csv_path)
    numeric_cols = ["logP", "qed", "SAS"]
    df = csv_path[numeric_cols].apply(pd.to_numeric, errors="coerce")
    st.write(df.describe())

    # Histogram for logP
    fig_hist, ax_hist = plt.subplots(figsize=(6, 4))
    sns.histplot(df["logP"].dropna(), bins=20, kde=True, color='#D65E3E')
    plt.title("Distribution of logP")
    plt.xlabel("logP")
    plt.ylabel("Frequency")

    # Display the histogram plot in Streamlit
    st.pyplot(fig_hist)

    # Scatter plot for logP vs qed
    fig_scatter, ax_scatter = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x="logP", y="qed", data=df)
    plt.title("Scatter Plot: logP vs qed")
    plt.xlabel("logP")
    plt.ylabel("qed")

    # Display the scatter plot in Streamlit
    st.pyplot(fig_scatter)

    # Correlation heatmap
    corr_matrix = df.corr()
    fig_heatmap, ax_heatmap = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr_matrix, annot=True, cmap="viridis", linewidths=.5)
    plt.title("Correlation Heatmap")

    # Display the heatmap in Streamlit
    st.pyplot(fig_heatmap)

elif choice == "Model":
    st.write("Molecule Generator Model 🧪 ")
    # Replace the path with the correct path to your image file
    image = st.image('/content/model 2.png', caption='The output is a list of molecular structures and generates a grid image to visualize these molecules.')
