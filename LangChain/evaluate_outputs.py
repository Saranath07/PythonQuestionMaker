import json
import re

def correct_json_string(json_string):
    # Replace single quotes with double quotes
    json_string = re.sub(r"(?<![\\])'", '"', json_string)
    
    # Handle cases where there might be unescaped single quotes within values
    # This is more complex and assumes there are no nested quotes within values.
    json_string = re.sub(r'(?<!")(\b\w+\b)(?!"):', r'"\1":', json_string)  # Keys without quotes
    json_string = re.sub(r':\s*(\b\w+\b)(?![,:])', r': "\1"', json_string)  # Values without quotes
    
    try:
        # Parse the corrected string into a JSON object
        json_object = json.loads(json_string)
        return json_object
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(json_string)
        print()
        return None

# Example usage
userQuestions = [
    "{'userConcept': 'functions', 'userInterest': 'tamil movies', 'problem_statement': 'Write a Python program to calculate the total box office collection of a list of Tamil movies.', 'function_name': 'calculate_total_collection', 'function_template': 'def calculate_total_collection(movies):\\n    # Your code here\\n    pass', 'test_cases': [{'input': ['Enthiran', 'Baahubali', 'Petta'], 'collection': [100, 200, 300], 'output': 600}, {'input': ['Viswaroopam', 'Kabali', '2.0'], 'collection': [50, 100, 250], 'output': 400}]}",
    '{"userConcept": "loops", "userInterest": "sports", "problem_statement": "Write a Python program to find the highest score in a list of cricket matches.", "function_name": "find_highest_score", "function_template": "def find_highest_score(scores):\\n    # Your code here\\n    pass", "test_cases": [{"input": [100, 150, 200], "output": 200}, {"input": [50, 75, 120], "output": 120}]}'
]

corrected_jsons = []
for i in range(len(userQuestions)):
    corrected_json = correct_json_string(userQuestions[i])
    if corrected_json:
        corrected_jsons.append(corrected_json)
        
        # Specify the file path
        file_path = f'output_{i}.json'
        
        # Write the JSON data to a file
        with open(file_path, 'w') as file:
            json.dump(corrected_json, file, indent=4)
        
        print(f"Data has been saved to {file_path}")
