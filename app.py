from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function - Load model and provide sql query as response
def get_gemini_response(question,prompt):

    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])

    return response.text


#Function - Retrieva data from database using the given query above
def read_sql_query(sql,db):

    conn =sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    return rows


#Define Your Prompt based on your db (change according to your db requirements)
#Prompt is in list form - you can give multiple prompts, remember to add it in the response above
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this - SELECT * FROM STUDENT
    where CLASS="Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

#Application
st.set_page_config(page_title="Siddharth's SQL Query Assistant")
st.header("Siddharth's Gemini-APP To Retrieve SQL Data")
question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")


#after submit is clicked
if submit:
    if question.strip() == "":  # Checking if question is empty or just spaces
        st.warning("Please ask a question before submitting.")
    else:
        response=get_gemini_response(question,prompt)
        print("The SQL Query is - ",response)
        response=read_sql_query(response,"student.db")
        st.subheader("The Response is")

        for row in response:
            print(row)
            st.header(row)





