# chatbot
 
# Chatbot Project

This project is a chatbot application built using Flask for the backend and React for the frontend. The chatbot can assist users with various tasks, provide information, and engage in friendly conversations. It includes features like natural language processing, spell check, information retrieval, and print functionality.

## Features

- **Natural Language Processing**: Understands and responds to user queries using advanced NLP techniques.
- **Information Retrieval**: Fetches relevant information from a predefined dataset and provides accurate responses.
- **Spell Check**: Corrects user input to ensure accurate responses.
- **Print Functionality**: Allows users to print the chat history, including shop details, with a single click.
- **User-Friendly Interface**: Intuitive and easy-to-use interface with features like clearing chat history and confirming print actions.

## Technologies Used

- **Backend**: Flask, NLTK, Scikit-learn, SpellChecker
- **Frontend**: React, Axios, Tailwind CSS, 

## Installation

### Backend

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatbot-project.git
    cd chatbot-project/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install flask
    pip install flask-cors
    pip install numpy
    pip install nltk
    pip install scikit-learn
    pip install pyspellchecker
    ```

4. Download NLTK Data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('brown')
    ```

5. Run the Flask server:
    ```bash
    python app.py
    ```

### Frontend

1. Navigate to the frontend directory:
    ```bash
    cd ../chatbot-frontend
    ```

2. Install the required packages:
    ```bash
    npm install
    ```

3. Configure Tailwind CSS:
    ```bash
    npx tailwindcss init -p
    ```

4. Add Tailwind Directives to CSS:
    Open the `src/index.css` file and add the following lines:
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

5. Start the React development server:
    ```bash
    npm start
    ```

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Interact with the chatbot by typing your messages in the input field and pressing Enter or clicking the "Send" button.
3. Use the "Clear Chat" button to clear the chat history.
4. Use the "Print Chat" button to print the chat history, including shop details.



