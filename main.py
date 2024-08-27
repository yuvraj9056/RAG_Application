from pdf_reader_fun import pdf_reader
from rag import run
import os
from dotenv import load_dotenv
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
print("Let's start ")
vector_db = pdf_reader(r"C:\Users\ranay\Desktop\llm\pdfs\BerkshireHillsBancorpInc_20120809_10-Q_EX-10.16_7708169_EX-10.16_Endorsement Agreement.pdf")
print("your data has been procesed")
query = input("enter your query")
ans = run(vector_db,query)
print(ans)