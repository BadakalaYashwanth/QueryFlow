LLM Streamlit SQL Gemini AI
This project is a Streamlit application that converts English questions into SQL queries using Google Gemini API and retrieves data from an SQLite database.

--![Screenshot 2024-07-03 134042](https://github.com/BadakalaYashwanth/LLM-Streamlit-Gemini-SQL-AI/assets/170221536/d6828ebf-5774-44aa-9977-b24cdf1a4f28)

--![Screenshot 2024-07-03 133328](https://github.com/BadakalaYashwanth/LLM-Streamlit-Gemini-SQL-AI/assets/170221536/3c45cf79-e6ba-4e62-b9b6-7663670ad508)

--![Screenshot 2024-07-03 133218](https://github.com/BadakalaYashwanth/LLM-Streamlit-Gemini-SQL-AI/assets/170221536/806cb7c3-c8f9-4470-9ef5-3f9c1ed96015)

--https://github.com/BadakalaYashwanth/LLM-Streamlit-Gemini-SQL-AI/assets/170221536/dfc351f8-bc91-48cf-8275-cd62b164a7b4

Description
This application leverages a large language model (LLM) via the Google Gemini API to translate natural language questions into SQL queries. The SQL queries are then executed against a SQLite database, and the results are displayed within the Streamlit app. The example dataset is stored in an SQLite database named EMPLOYEESDeails.db, which includes an EMPLOYEES table with various employee details.

Database Structure
The EMPLOYEESDeails.db SQLite database contains the following table:

EMPLOYEES
(Column Name)	          (Data Type)         	(Constraints),
EMPLOYEE_ID	            (INT),	             (PRIMARY KEY),
FIRST_NAME	         VARCHAR(50),	           (NOT NULL),
LAST_NAME	           VARCHAR(50),	           (NOT NULL),
EMAIL	               VARCHAR(100),	         (UNIQUE NOT NULL),
PHONE_NUMBER	       VARCHAR(20),	
HIRE_DATE             (DATE),	             (NOT NULL),
JOB_ID	             VARCHAR(10),	           (NOT NULL),
SALARY	             DECIMAL(8, 2),	
COMMISSION_PCT	     DECIMAL(2, 2),	
MANAGER_ID	           INT,	
DEPARTMENT_ID	         INT,	
DATE_OF_BIRTH	         DATE,	
ADDRESS	            VARCHAR(200),	
GENDER	            CHAR(1),	
NATIONALITY       	VARCHAR(50),
to retrieve data based on the generated SQL queries.



How to Use
Follow these steps to set up and run the application:

Prerequisites
Python 3.x
Streamlit
SQLite
Google Gemini API Key

requirements.txt
streamlit
google-generativeai 
python-dotenv
langchain
PyPDF2
chromadb
faiss-cpu
pdf2image
sqlite3

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
GOOGLE_API_KEY(Google Bard API Key)

4. Run the Streamlit app: Start the Streamlit server locally:
streamlit run app.py, This will launch the web application in your default web browser.                    

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
