# Cognitive Document LLM Aggregator

## Introduction
------------
The Cognitive Document LLM Aggregator is a Python application that allows you to chat with multiple documents. You can ask questions about the DOCs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## How It Works
------------

![Cognitive Document LLM Aggregator Diagram](./docs/PDF-LangChain.jpg)

The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation
----------------------------
To install the Cognitive Document LLM Aggregator, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies.
   
3. Obtain an API key from OpenAI
```

## Usage
-----
To use the Cognitive Document LLM Aggregator, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   or 
   python3 -m streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.

## Contributing
------------
This repository is intended for educational purposes and does not accept further contributions. It serves as supporting material for students to demonstrate how to build this project. Feel free to utilize and enhance the app based on your own requirements.

## License
-------
The Cognitive Document LLM Aggregator is released under the [MIT License](https://opensource.org/licenses/MIT).


gifs:-

https://i.ibb.co/9HD7L0n/QWsX.gif
https://i.ibb.co/r5CttzJ/globe-ezgif-com-crop.gif
https://i.ibb.co/hfrZ5Fs/spherewave.gif
https://ibb.co/FqjQmTT

https://i.ibb.co/3yJw4f8/3sstpm-1.png

5e0c0c
