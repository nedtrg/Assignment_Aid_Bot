# Assignment Aid Bot (AAB)


## Description

Assignment Aid Bot is an interactive chatbot built with Streamlit that assists with assignments by recognizing and responding to various prompts in user input. The bot uses OpenAI's GPT-3.5 and spaCy for natural language processing.

## Table of Contents

- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- Pitch Desk
- [License](#license)

## Pitch Desk: https://www.canva.com/design/DAGsMsIaHTo/rXSPaBdKH_2nHhcgdqb7dw/view?utm_content=DAGsMsIaHTo&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h27327fde6f

## Installation

Follow these steps to set up the project locally.

1. Clone the repository:
    ```bash
    git clone https://github.com/nedtrg/Assignment_Aid_Bot.git
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
