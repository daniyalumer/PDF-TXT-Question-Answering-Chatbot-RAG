# PDF/TXT Question Answering Chatbot

Welcome to the PDF/TXT Question Answering Chatbot repository! This project utilizes OpenAI's GPT-3.5 and LLAMA index to create a versatile chatbot capable of answering questions based on the contents of uploaded PDF or TXT documents.

## Key Features

- **Retrieval Augmented Generation (RAG)**: Enhances the accuracy and relevance of responses using advanced AI techniques.
- **PDF and TXT Support**: Allows users to upload and analyze documents in both PDF and TXT formats.
- **Interactive Chat Interface**: Enables users to engage in natural conversations with the chatbot, complete with conversational history.
- **GPT-like Interface**: Provides a familiar interface for seamless interaction and query responses.

## How It Works

1. **Upload Files**: Users can upload PDF or TXT files which are then processed to extract and index the content.
2. **Conversational History**: Tracks and displays previous interactions, allowing users to review and continue their conversations.
3. **AI-Generated Responses**: OpenAI's GPT-3.5 model generates accurate responses based on the indexed content, enhancing productivity and information retrieval.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pdf-txt-question-answering-chatbot.git
    cd pdf-txt-question-answering-chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your PDF/TXT files in the `data` directory.

2. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

3. Enter your OpenAI API key in the provided input field to initialize the chatbot.

4. Upload your PDF or TXT files through the interface and start asking questions!

## Project Structure

- `app.py`: Main application file.
- `data/`: Directory to store PDF/TXT files.
- `RPdata/`: Directory where uploaded files are saved.
- `requirements.txt`: List of dependencies required for the project.
- `prompt_chat2.txt`: Predefined prompt file used for initial conversation setup.





![Screenshot (166)](https://github.com/daniyalumer/PDF-TXT-Question-Answering-Chatbot-RAG/assets/96417048/1e9c1d7c-0472-42d9-b44a-6b042520ae65)
![Screenshot (167)](https://github.com/daniyalumer/PDF-TXT-Question-Answering-Chatbot-RAG/assets/96417048/1c485bd1-6b34-40b9-a8b9-938a158289c5)

