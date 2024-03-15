from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import pinecone
import asyncio
import itertools
from langchain.document_loaders.sitemap import SitemapLoader

##### FETCH DATA FROM WEBSITE - START #####
'''
More info about SitemapLoader at:
https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/sitemap
'''
def get_website_data(sitemap_url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loader = SitemapLoader(sitemap_url)
    
    docs = loader.load()
    return docs


##### FETCH DATA FROM WEBSITE - END #####

##### SPLIT DATA INTO CHUNKS - START #####

def split_data(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    docs_chunks = text_splitter.split_documents(docs)
    return docs_chunks

##### SPLIT DATA INTO CHUNKS - END #####

##### CREATE EMBEDDINGS - START #####

def create_embeddings():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

##### CREATE EMBEDDINGS - END #####

##### PUSH DATA TO PINECONE - START #####

def push_to_pinecone(pinecone_api_key, pinecone_environment, 
                    pinecone_index_name, embeddings, docs):
    
    pinecone.init(
        api_key = pinecone_api_key,
        environment = pinecone_environment    
    )
    
    index_name = pinecone_index_name
    index = Pinecone.from_documents(docs, embeddings, index_name = index_name)
    
    return index

##### PUSH DATA TO PINECONE - END #####