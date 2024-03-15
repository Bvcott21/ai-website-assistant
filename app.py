import streamlit as st
from utils import *
import constants

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
        site_data = get_website_data(constants.WEBSITE_URL)
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
            st.session_state['Pinecone_API_Key'],
            constants.PINECONE_ENV,
            constants.PINECONE_INDEX,
            embeddings,
            chunks_data
        )
        st.write("Pushing data to Pinecone...")
        
        st.sidebar.success("Data pushed to Pinecone successfully!")
        
    else:
        st.sidebar.error("Please provide API Keys")
        
##### SIDE BAR - END #####

##### CAPTURE USER INPUT - START #####

prompt = st.text_input("How can I help?", key = "prompt") # The box for the text prompt
document_count = st.slider(
    "No. of links to return = (0 - LOW || 5 - HIGH)", 
    0, 5, 2, 
    step = 1
)

submit = st.button("Search")

if submit:
    # Proceed only if API Keys are provided
    if st.session_state['HuggingFace_API_Key'] != "" and st.session_state['Pinecone_API_Key'] != "":
        # Create embeddings instance
        embeddings = create_embeddings()
        st.write("Embeddings instance created")
    
        # Pull index data from Pinecone
        index = pull_from_pinecone(
            st.session_state['Pinecone_API_Key'],
            constants.PINECONE_ENV,
            constants.PINECONE_INDEX,
            embeddings
        )
        st.write("Pinecone index retrieval")
        
        # Fetch relevant documents from Pinecone
        similar_docs = get_similar_docs(index, prompt, document_count)
        
        # Displaying search result
        for document in similar_docs:
            st.write("**Result : " + str(similar_docs.index(document) + 1) + "**")
            st.write("**Info**:" + document.page_content)
            st.write("**Link**:" + document.metadata['source'])
        
        st.success("Search results: ")
##### CAPTURE USER INPUT - END #####