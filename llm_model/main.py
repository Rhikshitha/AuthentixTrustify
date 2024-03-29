from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
vector_store = FAISS.load_local("D:/Projects/AuthentixTrustify/llm_model/faiss_vector_db", embeddings=embeddings) 
repo_id = 'tiiuae/falcon-7b-instruct'
llm = HuggingFaceHub(
    repo_id=repo_id,
    model_kwargs = {
        "temperature": 0.1,
        "max_new_tokens":500,
    },
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vector_store.as_retriever(),
    return_source_documents = True,
)

def generate_answer(query):
    answer_set = qa(query)["result"]
    try:
        answer = answer_set[answer_set.rindex("Helpful Answer: ")+len("Helpful Answer: "):]
    except:
        answer="Oops! There has been some technical problem in the backend. Please try again."
    return answer









# if __name__ == "__main__":
#     load_dotenv()
#     embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
#     vector_store = FAISS.load_local("faiss_vector_db", embeddings=embeddings) 
#     repo_id = 'tiiuae/falcon-7b-instruct'
#     llm = HuggingFaceHub(
#         repo_id=repo_id,
#         model_kwargs = {
#             "temperature": 0.1,
#             "max_new_tokens":500,
#         },
#     )
#     print("before prompt")

#     qa = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type='stuff',
#         retriever=vector_store.as_retriever(),
#         return_source_documents = True,
#     )
    


#     prompt = input("Enter your question/ enter q to quit: ")
#     while prompt != "q":
#         res = qa(prompt)
#         print("\n----------------\n")
#         print("Question: ", prompt)
#         print("\n",res["result"])
#         print("\n----------------\n")
        
#         prompt = input("Enter your question/ enter q to quit: ")
    