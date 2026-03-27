# test_ai_medium.py

import langchain
import weaviate
import chromadb
import autogen
import openai
import torch
from crewai import Agent
from langchain.utilities import SQLDatabase
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader, TextLoader, CSVLoader

# langchain-sql-database-chain     # 1 
db = langchain.utilities.SQLDatabase(engine)
##########

# chromadb-persistent-no-auth     # 2
client = chromadb.PersistentClient(path="./chroma_db")
##########

# autogen-code-execution-enabled  # 3
assistant = autogen.AssistantAgent(
    name="assistant",
    code_execution_config={"work_dir": "coding"}
)
#########

# crewai-code-execution-enabled    # 4
agent = Agent(
    role="developer",
    goal="write code",
    allow_code_execution=True
)

##############

# rag-document-injection   # 5
loader1 = PyPDFLoader(user_provided_path)
loader2 = TextLoader(file_path)
loader3 = CSVLoader(request_path)

##################
# weaviate-no-auth   # 6
weaviate_client = weaviate.connect_to_wcs(
    cluster_url="https://my-cluster.weaviate.network"
)

###################3
# rag-no-content-filtering
chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)





# test_ai_hard.py

import openai
from langchain.prompts import load_prompt
from langchain.chains import PALChain, LLMMathChain


#########

# langchain-load-prompt-rce    # 1
prompt = load_prompt("http://external-site.com/prompt.json")

#############
# autogen-no-docker-isolation   # 2
config = {"use_docker": False, "work_dir": "coding"}

################################
# safetensors-preferred       # 3
model = torch.load("model.pt")

#############################
# streaming-response-no-validation   # 4
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "hello"}],
    stream=True
)

###########################


# langchain-pal-chain-rce    # 5
chain = PALChain(llm=llm)
math_chain = LLMMathChain(llm=llm)

#######################

# function-calling-no-validation  # 6
openai.ChatCompletion.create(
    model="gpt-4",
    messages=[],
    functions=my_functions
)

###########################



