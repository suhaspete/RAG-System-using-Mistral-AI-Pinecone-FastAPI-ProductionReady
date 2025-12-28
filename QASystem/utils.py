#this is the file that performs specific task and can be utilised across various functionalities

from haystack_integrations.document_stores.pinecone import PineconeDocumentStore #used for storing the embeddings of documents in the vector store 
import os
from dotenv import load_dotenv

#loading the environment variable
load_dotenv() 

#reading the env variable
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

#setting the environ variable temporarily and can be used throughout the execution. 
os.environ['PINECONE_API_KEY'] =PINECONE_API_KEY

print("Import successfully")

def pinecone_config():
    #configuring pinecone database
    document_store = PineconeDocumentStore(
         environment="gcp-starter", #region of the server
            index="default",
            namespace="default",
            dimension=768


    )
    print("Import successfully")
    return document_store

