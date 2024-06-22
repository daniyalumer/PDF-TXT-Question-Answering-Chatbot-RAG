import streamlit as st
from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
import os
import PyPDF2  # PyPDF2 for PDF text extraction

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to construct the index
def construct_index(directory_path, api_key):
    max_input_size = 4096
    num_outputs = 2000
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo", max_tokens=num_outputs, openai_api_key=api_key))

    documents = SimpleDirectoryReader(directory_path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
    index.save_to_disk('index.json')

    return index

# Streamlit app
st.title("Research Paper Question Answering Application")

# Initialize session state for API key and index
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

if "index" not in st.session_state:
    st.session_state.index = None

# API key input
st.header("Enter your OpenAI API key")
api_key_input = st.text_input("OpenAI API Key", type="password")
if st.button("Submit API Key"):
    st.session_state.api_key = api_key_input

if st.session_state.api_key:
    # Initialize the index if it's not already
    if st.session_state.index is None:
        st.session_state.index = construct_index("data", st.session_state.api_key)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Read content from prompt_chat.txt
    prompt_chat_file_path = "prompt_chat2.txt"
    if os.path.exists(prompt_chat_file_path):
        with open(prompt_chat_file_path, "r", encoding="utf-8") as file:
            predefined_prompt = file.read()
    else:
        predefined_prompt = "Default prompt if prompt_chat2.txt is not found."

    # File Upload Section
    st.header("Upload a Text or PDF File")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

    if uploaded_file is not None:
        # Save the uploaded file to the data directory
        file_path = os.path.join("RPdata", uploaded_file.name)
        with open(file_path, "wb") as file:
            file.write(uploaded_file.read())
        
        if uploaded_file.type == "application/pdf":
            # Extract text from the PDF file
            text = extract_text_from_pdf(file_path)
            # Save the extracted text to a txt file for indexing
            text_file_path = file_path.replace(".pdf", ".txt")
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)
        else:
            text_file_path = file_path

        st.success(f"File uploaded successfully: {uploaded_file.name}")

        # Optionally, you can update the index with the new data
        st.session_state.index = construct_index("RPdata", st.session_state.api_key)

        # Display a message about the uploaded file
        with open(text_file_path, "r", encoding="utf-8") as file:
            st.info(f"Uploaded file content")

    # User Input Section
    prompt = st.text_input("You:")

    if st.button("Submit"):
        if prompt:
            # Combine user input with predefined prompt
            combined_prompt = f"{predefined_prompt}\nUser: {prompt}"

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                # Call OpenAI API to get assistant's response
                response = st.session_state.index.query(combined_prompt)

                # Display the assistant's response
                st.markdown(response.response)

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response.response})
else:
    st.warning("Please enter your OpenAI API key.")
