# rag.py
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from groq import Groq
from pdf_reader_fun import pdf_reader

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def run(vectordb, query, template):
    print("Starting retrieval and generation process...")
    retriever = vectordb.as_retriever()

    # Define a custom prompt template for legal analysis
    prompt = PromptTemplate(template=template,
                            input_variables=['context', 'query'])

    llm = ChatGroq(model="llama3-8b-8192", groq_api_key=api_key)
    
    rag_chain = (
        {"context": retriever, "query": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Make sure to pass the correct input keys for the prompt
    return rag_chain.invoke(query)

prompt_template = "You are a legal expert. Using the provided data: {context}, can you address the question: {query}?"
query = "Who are the parties involved in this endorsement agreement?"
vectordb = pdf_reader(r"C:\Users\ranay\Desktop\llm\pdfs\BerkshireHillsBancorpInc_20120809_10-Q_EX-10.16_7708169_EX-10.16_Endorsement Agreement.pdf")
print(run(vectordb, query, prompt_template))

