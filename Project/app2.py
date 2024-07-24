import gradio as gr
import json

# Function to read a JSON file
data = {
        "problem_statement": "Write a function that adds two numbers.",
        "function_template": "def add_numbers(a, b):\n    # Your code here",
        "test_cases": [
            {"input": "1, 2", "output": "3"},
            {"input": "10, 20", "output": "30"}
        ],
        "function_name": "add_numbers"
    }

question = data['problem_statement']
function_template = data['function_template']
function_template = function_template.replace("\\n", "\n")
test_cases = data['test_cases']

# Function to run the user code
def run_code(code):
    outputs = []
    try:
        # Extract necessary information
        function_name = data["function_name"]
        
        # Prepare the global namespace for the execution
        exec_globals = {}
        exec(code, exec_globals)
        
        # Retrieve the function from the user's code
        func = exec_globals.get(function_name)
        
        if not func:
            return [f"Function '{function_name}' not found."] * 2

        # Run all test cases
        for test_case in test_cases:
            inputs = list(map(int, test_case["input"].split(", ")))
            expected_output = int(test_case["output"])

            # Execute the function with the test case inputs
            result = func(*inputs)
            output = f"Input: {test_case['input']}\nOutput: {result}, Expected: {expected_output}"
            outputs.append(output)
    except Exception as e:
        outputs = [f"An error occurred: {str(e)}"] * 2
    
    return outputs

# Function to create the first page
def create_first_page():
    with gr.Column() as page1:
        user_name = gr.Textbox(label="Enter your name")
        next_button = gr.Button("Next")
        return page1, next_button

# Function to create the second page
def create_second_page():
    with gr.Column(visible=False) as page2:
        user_interest = gr.Textbox(label="Enter your interest")
        next_button = gr.Button("Next")
        return page2, next_button

# Function to create the third page
def create_third_page():
    with gr.Column(visible=True) as page3:
        with gr.Row():
            with gr.Column():
                question_display = gr.Textbox(label="Question", value=question, interactive=False)
                input_box1 = gr.Textbox(label="Input for Test Case 1", value=test_cases[0]['input'], interactive=False)
                input_box2 = gr.Textbox(label="Input for Test Case 2", value=test_cases[1]['input'], interactive=False)
                code_input = gr.Code(label="Write your code here", language="python", value=function_template)
                run_button = gr.Button("Run")
            
            with gr.Column():
                output_box1 = gr.Textbox(label="Output for Test Case 1")
                output_box2 = gr.Textbox(label="Output for Test Case 2")
        
        run_button.click(fn=run_code, inputs=code_input, outputs=[output_box1, output_box2])
    
    return page3


# if __name__ == "__main__":
#     with gr.Blocks() as app:
#         page1, next_button1 = create_first_page()
#         page2, next_button2 = create_second_page()
#         page3 = create_third_page()

#         state = gr.State()

#         def show_page2():
#             state.value = 2
#             return [gr.update(visible=False), gr.update(visible=True)]

#         def show_page3():
#             state.value = 3
#             return [gr.update(visible=False), gr.update(visible=True)]

#         next_button1.click(show_page2, inputs=None, outputs=[page1, page2])
#         next_button2.click(show_page3, inputs=None, outputs=[page2, page3])

#     app.launch()
