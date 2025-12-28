from haystack import Pipeline #collection of components. 
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter #used for chunking like recursivesplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder #for creating embeddings
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore #storing the document
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv

from QASystem.utils import pinecone_config

#creating the ingest method

def ingest(document_store):

    indexing = Pipeline()

    #adding the components in the pipeline

    indexing.add_component("converter",PyPDFToDocument())  #load the data
    indexing.add_component("splitter",DocumentSplitter(split_by="sentence",split_length=2)) #split the document by sentence and each split will have 2 sentences. #chunking
    indexing.add_component("embedder",SentenceTransformersDocumentEmbedder()) #embediing
    indexing.add_component("writer",DocumentWriter(document_store)) #used for writing the document in the pinecone.  #for that pinecone configuration would be required.


    #conencting the components

    indexing.connect("converter","splitter")
    indexing.connect("splitter","embedder")
    indexing.connect("embedder","writer")

    #storing the pdf data as an embedding in the database. 
    #reading the data from the database. 

    indexing.run(
        
        {"converter":
         
         {"sources": 
          
          [Path(r"C:\Genesilico\End-to-End-RAG-Application-Using-Haystack-MistralAI-Pinecone-FastAPI\data\Retrieval-Augmented-Generation-for-NLP.pdf")]
          
          
          }
         
         
         }
        
        
        )





if __name__ == "main": #writing this if we want to call this method seprately
    document_store=pinecone_config() #calling the pinecone_config to get the document store. 
    
    
    ingest(document_store) #calling the ingest method