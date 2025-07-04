# Clear Your Doubts(CYD) Bot


## Description

Homework Helper Bot is an interactive chatbot built with Streamlit that assists with homework by recognizing and responding to various patterns in user input. The bot uses OpenAI's GPT-3.5 and spaCy for natural language processing.

## Table of Contents

- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- Pitch Desk
- [License](#license)

## Pitch Desk: https://gamma.app/docs/Homework-Helper-Empowering-Parents-Enriching-Learning-idu04yxqo6o1kw8
## Video: https://drive.google.com/file/d/1yVEIBUePNoVM4S1fNrUkWJgp8BzjOh3P/view?usp=sharing

## Installation

Follow these steps to set up the project locally.

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/homework-helper-bot.git
    cd homework-helper-bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up OpenAI API Key:
    - Create a `.env` file in the project root.
    - Add your OpenAI API key:
        ```env
        OPENAI_API_KEY=your-openai-api-key
        ```

## Usage

To run the application:

```bash
streamlit run app.py
