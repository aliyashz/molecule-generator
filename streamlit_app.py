import streamlit as st

def home():
    st.title("Home")
    st.write("Welcome to the Home tab!")
    st.write("This is a paragraph of text for the Home tab.")
    # Add more content as needed

def about():
    st.title("About")
    st.write("This is the About tab.")
    st.write("Here, you can provide information about your app or project.")
    # Add more content as needed

def analysis():
    st.title("Analysis")
    st.write("Explore your data in the Analysis tab.")
    st.write("You can add charts, graphs, and insights here.")
    # Add more content as needed

def model():
    st.title("Model")
    st.write("Train and deploy your model in the Model tab.")
    st.write("This tab can include information about your machine learning model.")
    # Add more content as needed

# Create tabs

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


# Display the selected tab content
if selected_tab == "Home":
    home()
elif selected_tab == "About":
    about()
elif selected_tab == "Analysis":
    analysis()
elif selected_tab == "Model":
    model()
