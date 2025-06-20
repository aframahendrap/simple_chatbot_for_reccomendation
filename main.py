import getpass
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
#Checking GOOGLE API KEY in environment
load_dotenv()

#LLM MODEL
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    max_output_tokens=None,
    temperature=0.7,
    max_retries=2,
    timeout=None
)

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        #INTRODUCTION
        You are an assistant who helps patients to provide departmental recommendations for treatment 
        based on the symptoms of the disease given by the patient.

        #USER INPUT
        User input in the form of name, age, and symptoms of the disease experienced.
         
        #HOW TO ANSWER
        1. Analyze the disease based on the symptoms inputted by the user.
        2.  The answer is the name of the department that matches the symptoms of the disease inputted by the user.
        3.  The output must be in JSON format.
        4.  Please answer in English. 
         
        
         """),
        ("human", "{input}"),
    ]
)
#chainning
chain = prompt | llm

#API setup
app = FastAPI()
@app.post("/department_recommendation")
async def get_department_recommendation(gender: str, age: int, symptoms: str) -> str:
    try:
        user_input = f"Gender: {gender}, Age: {age}, Symptoms: {symptoms}"
        response = chain.invoke({"input": user_input})
        return response.content 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Department Recommendation API"}