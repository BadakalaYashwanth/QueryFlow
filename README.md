LLM Streamlit SQL Gemini AI

Overview
LLM Streamlit SQL Gemini AI is a Streamlit web application that leverages Google's Generative AI (Gemini) to convert English questions into SQL queries. It also interacts with an SQLite database (EMPLOYEESDeails.db) 
to retrieve data based on the generated SQL queries.

Features
Converts English questions to SQL queries using Google's Generative AI.
Executes SQL queries on the SQLite database (EMPLOYEESDeails.db) to fetch relevant data.
Provides a user-friendly interface using Streamlit for inputting questions and displaying SQL query results.

Installation
1. Clone the repository:
git clone https://github.com/yourusername/llm-streamlit-sql-gemini-ai.git
cd llm-streamlit-sql-gemini-ai

2. Install dependencies:
Ensure you have Python 3.6+ installed. Install required packages using pip:
pip install -r requirements.txt

3. Set up environment variables:
Create a .env file in the root directory and add your Google API key:
GOOGLE_API_KEY="your_google_api_key"

4. Run the Streamlit app: Start the Streamlit server locally:
streamlit run app.py , This will launch the web application in your default web browser.                    

Usage

1. Input your question:
Enter an English question related to the EMPLOYEES database into the text box provided.

2. Generate SQL query:
Click on the "Ask the question" button to generate the corresponding SQL query using Google's Generative AI.

3. View SQL query response:
The application will display the SQL query generated and execute it against the EMPLOYEESDeails.db SQLite database. Results will be shown below the input box.

4. Explore different queries:
Try different types of questions (e.g., aggregate functions, filters) to see how the application generates SQL queries and retrieves data.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.
