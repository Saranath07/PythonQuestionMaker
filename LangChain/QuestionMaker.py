# LangChain imports

from langchain.chains import SimpleSequentialChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from langchain_groq import ChatGroq

import random
import json
import os
import sys

with open('apiKeys.json', 'r') as file:
    apiKeys = json.load(file)





os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = apiKeys['LANGCHAIN_API_KEY']
os.environ["GROQ_API_KEY"] = apiKeys['GROQ_API_KEY']
class QuestionMaker:

    def __init__(self, userConcepts, userInterests, model_name="llama3-8b-8192"):

        self.userConcepts = userConcepts
        self.userInterests = userInterests
        self.model = ChatGroq(model=model_name)


    def frame_a_question(self, userConcept, userInterest):
        
        
      
        with open("example_jsons/template_1.json", "r") as f:
            template_1 = str(json.load(f))
        
        # print(type(template_1))
        
        with open("example_jsons/template_2.json", "r") as f:
            template_2 = str(json.load(f))
        
        
        messages = [
            SystemMessage(content=f"""
            Generate a valid python programming question with 2 or more test cases for the given 
            concept and theme in json format strictly without any other extra sentances. STRICTLY USE DOUBLE QUOTES \"\" for JSON PARSABLE IN PYTHON.
            """),
            HumanMessage(content=f"Concept : functions, Theme : cricket"),
            AIMessage(content=template_1),
            HumanMessage(content=f"Concept : file handling, Theme : fruits"),
            AIMessage(content=template_2),
            HumanMessage(content=f"Concept : {userConcept}, Theme : {userInterest}")
        ]

        return self.model.invoke(messages).content

    def get_questions(self, n):

        questions = set()

        while len(questions) < n:
            userConcept = random.choice(self.userConcepts)
            userInterest = random.choice(self.userInterests)
            question = self.frame_a_question(userConcept, userInterest)
            questions.add(question)

        return list(questions)


with open("example_jsons/user_json.json", "r") as f:
    user_json = json.load(f)

questionMaker = QuestionMaker(user_json[0]["userConcepts"], user_json[0]["userInterests"])

userQuestions = questionMaker.get_questions(10)

for i in range(len(userQuestions)):

    with open("outputs/question_"+str(i+1)+".json", "w") as f:
        json.dump(userQuestions[i], f, indent=4)


          

        

        
        