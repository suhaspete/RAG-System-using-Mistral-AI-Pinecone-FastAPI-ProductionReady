from haystack.utils import Secret #used for storing the api keys
from haystack.components.embedders import SentenceTransformersTextEmbedder #used for embeddings
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever #to retrive the data from pinecone
from haystack.components.generators import HuggingFaceTGIGenerator #used for accessing the llm model
from haystack import Pipeline

import os
from dotenv import load_dotenv

from QASystem.utils import pinecone_config

prompt_template = """Answer the following query based on the provided context. If the context does
                     not include an answer, reply with 'I don't know'.\n
                     Query: {{query}}
                     Documents:
                     {% for doc in documents %}
                        {{ doc.content }}
                     {% endfor %}
                     Answer: 
                  """


#this method will give the response based on the query that we provide. 

def get_result(query):
    query_pipeline = Pipeline()

    #add component
    query_pipeline.add_component("text_embedder", SentenceTransformersTextEmbedder()) #embedding the query
    query_pipeline.add_component("retriever", PineconeEmbeddingRetriever(document_store=pinecone_config())) #retriever the relevant doc based on similarity search
    query_pipeline.add_component("prompt_builder",PromptBuilder(template=prompt_template) )
    query_pipeline.add_component("llm",HuggingFaceTGIGenerator(model="mistralai/Mistral-7B-v0.1", token=Secret.from_token("token id")))

    #combining the documents
    query_pipeline.connect("text_embedder.embedding","retriever.query_embedding")
    query_pipeline.connect("retriever.documents", "prompt_builder.documents")
    query_pipeline.connect("prompt_builder","llm")

    results = query_pipeline.run(
        {

            "text_embedder" : {"text":query},
            "prompt_builder" : {"query":query}


    }
    
    )

    return results['llm']['replies'][0]
 


if __name__=="main":
    result=get_result("what is rag token?")

    print(result)