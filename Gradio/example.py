import os
import json

parent_directory = os.path.join('..', 'outputs')

def read_generated_files():
    files = []
    for file_name in os.listdir(parent_directory):
        if file_name.startswith("question_") and file_name.endswith(".json"):
            with open(os.path.join(parent_directory, file_name), "r", encoding='utf-8') as f:
                files.append(json.load(f))
    return files

files = read_generated_files()
for f in files:
    print(f["problem_statement"])
    print()