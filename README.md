# SQL Query Assistant

## Overview
SQL Query Assistant is a Streamlit-based application designed to convert English questions into SQL queries. Using Google's Generative AI, this tool makes it easier to interact with databases by simplifying the query generation process.

## Features
- Converts natural language questions into SQL queries.
- Executes queries on a SQLite database and displays results.
- Built with Streamlit, offering a responsive user interface.
- Customizable prompts to fit different database schemas.

## Getting Started

### Prerequisites
- Python 3.6+
- Streamlit
- SQLite3
- Google Generative AI package

### Installation
1. Clone the repository.
2. Navigate to the directory.
3. Install required packages using `pip install -r requirements.txt`.

### Configuration
Set up your Google Generative AI API Key in a `.env` file.

### Usage
Run the Streamlit app with `streamlit run app.py`. Enter your question in the text field and click "Ask the question" to get the SQL query and results.

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first.

## License
This project is under the MIT License.

## Acknowledgments
- Google's Generative AI for the AI model.
- Streamlit team.
