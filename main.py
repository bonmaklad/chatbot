import os
import sys
import constants 

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

loader = DirectoryLoader("./data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

#only the data from the document 
print(index.query(query))

#including chatgpt library 
#print(index.query(query, llm=ChatOpenAI()))