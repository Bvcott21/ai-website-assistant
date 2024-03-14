import streamlit as st
from utils import *

# Creating session state variables
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] = ''
if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['Pinecone_API_Key'] = ''

st.title('🤖 AI Assistant for Website')

##### SIDE BAR - START #####

# Sidebar to capture the API Keys
st.sidebar.title("🗝")
st.session_state['HuggingFace_API_Key'] = st.sidebar.text_input(
    "What's your HuggingFace API key?", 
    type = "password"
)

st.session_state['Pinecone_API_Key'] = st.sidebar.text_input(
    "What's your Pinecone API Key?",
    type = "password"
)

load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

# If the above button is clicked, pushing the data to Pinecone
if load_button:
    # Proceed only if the API Keys are provided
    if st.session_state['HuggingFace_API_Key'] != "" and st.session_state['Pinecone_API_Key'] != "": 
        
        # Fetch data from site
        site_data = get_website_data("https://jobs.excelcult.com/wp-sitemap-posts-post-1.xml")
        st.write("Data pull done...")
        
        # Split data into chunks
        chunks_data = split_data(site_data)
        st.write("Splitting data done...")
        
        # Creating embeddings instace
        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")
        
        # Push data to Pinecone
        # Dimensions utilized for Pinecone index creation: 384 - Metric: Cosine
        push_to_pinecone(
            st.session_data['Pinecone_API_Key'],
            "gcp-starter",
            "chatbot",
            embeddings,
            chunks_data
        )
        st.write("Pushing data to Pinecone...")
        
        st.sidebar.success("Data pushed to Pinecone successfully!")
        
    else:
        st.sidebar.error("Please provide API Keys")
        
##### SIDE BAR - END #####