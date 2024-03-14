from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import pinecone
import asyncio
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
