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
