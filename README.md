
# Text RAG Application

This project is a Text Retrieval-Augmented Generation (RAG) application that takes a PDF as input from the user and answers queries using a Large Language Model (LLM). The RAG application is built using the Langchain framework and provides a user-friendly interface for querying documents.

## Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Technologies Used](#technologies-used)
- [Flowchart of the Application](#flowchart-of-the-application)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This application enables users to upload a PDF document, from which the text is chunked and embedded. The user can then query the document, and the application will retrieve relevant chunks using a vector database and generate answers using an LLM. The core functionality is powered by Langchain, with components for chunking, embedding, retrieval, and answer generation.

## Repository Structure
- **`rag.py`**: Contains the code for retrieval and answer generation using the Langchain framework.
- **`pdf_reader.py`**: Handles reading the PDF input from the user, chunking the text using `RecursiveCharacterTextSplitter`, and generating embeddings with `HuggingFaceEmbeddings`.
- **`main.py`**: Contains the code for the Streamlit application, including the user interface and interaction flow for uploading PDFs and querying the document.

## Technologies Used
- **Langchain**: Framework for building LLM-powered applications.
- **RecursiveCharacterTextSplitter**: Used for splitting the text into chunks for efficient retrieval.
- **HuggingFaceEmbeddings**: Used to generate embeddings from the text chunks.
- **Chroma**: Vector database used for storing and retrieving the text embeddings.
- **Llama3 from Groq**: Large Language Model used for generating answers based on the retrieved chunks.
- **Streamlit**: Framework for building the web-based user interface of the application.

## Flowchart of the Application
![rag flow_page-0001](https://github.com/user-attachments/assets/ee9e3a1a-e025-43d5-b91b-b7411403d590)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-rag-application.git
    cd text-rag-application
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that your environment is configured with the necessary API keys and credentials for the LLM and embeddings.

## Usage
1. **Run the Streamlit Application**:
    Start the Streamlit application to interact with the RAG model through a simple UI.
    ```bash
    streamlit run main.py
    ```

2. **Upload a PDF**:
    Upload a PDF file through the Streamlit UI.

3. **Query the Document**:
    After the PDF is processed, you can enter your query in the UI. The system will retrieve relevant chunks and generate an answer using the LLM.

## Future Work
- **Deployment**: Working on deploying the application to a cloud platform for public access.
- **Model Optimization**: Exploring methods to optimize the retrieval and generation process for better performance.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License.

---

You can modify the details as per your needs and include the flowchart in the appropriate section.
