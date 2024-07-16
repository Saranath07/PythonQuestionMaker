# LangChain imports

from langchain.chains import SimpleSequentialChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from langchain_groq import ChatGroq

import random
import json
import os

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
        problem_statement_1 = "Write a python program to add the total scores of the batsman in his two innings"
        function_name_1 = "add"
        function_template_1 = "def add_scores(score1, score2):\\n    # Your code here\\n    pass"
        test_cases_1 = [
            {
                "input": "10, 20",
                "output": "30"
            },
            {
                "input": "46, 52",
                "output": "98"
            }
        ]
        
        example_output_1 = f"""
        {{
            "userConcept" : "functions",
            "userInterest" : "cricket"
            "problem_statement": "{problem_statement_1}",
            "function_name": "{function_name_1}",
            "function_template": "{function_template_1}",
            "test_cases": [
                {{
                    "input": "{test_cases_1[0]['input']}",
                    "output": "{test_cases_1[0]['output']}"
                }},
                {{
                    "input": "{test_cases_1[1]['input']}",
                    "output": "{test_cases_1[1]['output']}"
                }}
            ]
        }}
        """
        
        problem_statement_2 = "Write a Python program to read a file named 'fruits.txt' and list out all the fruits in a python list."
        function_name_2 = "display_fruits"
        function_template_2 = "def display_fruits(filename):\\n    # Your code here\\n    pass"
        test_cases_2 = [
            {
                "input": "fruits.txt",
                "content" : "apple \\n mango \\n banana",
                "output": "['apple', 'mango', 'banana']"
            },
            {
                "input": "fruits.txt",
                "content" : "blueberry \\n strawberry \\n raspberry",
                "output": "['blueberry', 'strawberry', 'raspberry']"
            }
        ]
        
        example_output_2 = f"""
        {{
            "userConcept" : "file handling",
            "userInterest" : "fruits"
            "problem_statement": "{problem_statement_2}",
            "function_name": "{function_name_2}",
            "function_template": "{function_template_2}",
            "test_cases": [
                {{
                    "input": "{test_cases_2[0]['input']}",
                    "content" : "{test_cases_2[0]['content']}",
                    "output": "{test_cases_2[0]['output']}"
                }},
                {{
                    "input": "{test_cases_2[1]['input']}",
                    "content" : "{test_cases_2[1]['content']}",
                    "output": "{test_cases_2[1]['output']}"
                }}
            ]
        }}
        """
        
        
        messages = [
            SystemMessage(content=f"""
            Generate a valid python programming question with 2 or more test cases for the given 
            concept and theme in json format strictly without any other extra sentances.
            """),
            HumanMessage(content=f"Concept : functions, Theme : cricket"),
            AIMessage(content=example_output_1),
            HumanMessage(content=f"Concept : file handling, Theme : fruits"),
            AIMessage(content=example_output_2),
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
            

        

        
        