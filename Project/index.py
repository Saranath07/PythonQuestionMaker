import gradio as gr
import os
import json
from PythonQuestionMaker import QuestionMaker


def create_third_page(data):
    with gr.Column(visible=False) as page3:
        with gr.Row():
            question_select = gr.Dropdown(label="Select Question", choices=[d['problem_statement'] for d in data], interactive=True)
            question_display = gr.Textbox(label="Question", interactive=False)
        
        # Display test case inputs in separate boxes
        input_box1 = gr.Textbox(label="Input for Test Case 1", interactive=False)
        input_box2 = gr.Textbox(label="Input for Test Case 2", interactive=False)

        code_input = gr.Code(label="Write your code here", language="python")
        output_box1 = gr.Textbox(label="Output for Test Case 1")
        output_box2 = gr.Textbox(label="Output for Test Case 2")
        run_button = gr.Button("Run")

        def update_question(selected_question):
            selected_data = next(d for d in data if d['problem_statement'] == selected_question)
            return (selected_data["problem_statement"],
                    selected_data['test_cases'][0]['input'],
                    selected_data['test_cases'][1]['input'],
                    selected_data['function_template'])

        def run_code(code, selected_question):
            outputs = []
            try:
                selected_data = next(d for d in data if d['problem_statement'] == selected_question)
                function_name = selected_data["function_name"]
                
                # Prepare the global namespace for the execution
                exec_globals = {}
                exec(code, exec_globals)
                
                # Retrieve the function from the user's code
                func = exec_globals.get(function_name)
                
                if not func:
                    return [f"Function '{function_name}' not found."] * 2

                # Run all test cases
                for test_case in selected_data['test_cases']:
                    inputs = list(map(int, test_case["input"].split(", ")))
                    expected_output = int(test_case["output"])

                    # Execute the function with the test case inputs
                    result = func(*inputs)
                    output = f"Input: {test_case['input']}\nOutput: {result}, Expected: {expected_output}"
                    outputs.append(output)
            except Exception as e:
                outputs = [f"An error occurred: {str(e)}"] * 2
            
            return outputs

        question_select.change(fn=update_question, inputs=question_select, outputs=[question_display, input_box1, input_box2, code_input])
        run_button.click(fn=run_code, inputs=[code_input, question_select], outputs=[output_box1, output_box2])
        
    return page3

data = [
    {
        "problem_statement": "Sum of two numbers",
        "function_name": "add",
        "function_template": "def add(a, b):\n    pass",
        "test_cases": [
            {"input": "1, 2", "output": "3"},
            {"input": "3, 4", "output": "7"}
        ]
    },
    {
        "problem_statement": "Multiply two numbers",
        "function_name": "multiply",
        "function_template": "def multiply(a, b):\n    pass",
        "test_cases": [
            {"input": "2, 3", "output": "6"},
            {"input": "4, 5", "output": "20"}
        ]
    }
]

with gr.Blocks() as demo:
   
    with gr.Column(visible=True) as page1:
        gr.Markdown("### Page 1: User Details")
        name = gr.Textbox(label="Name")
        roll_no = gr.Textbox(label="Roll Number")
        submit1 = gr.Button("Submit")
        result1 = gr.Text()
        
    with gr.Column(visible=False) as page2:
        gr.Markdown("### Page 2: Theme and Topic Selection")
        theme = gr.Textbox(label="Select theme")
        topic = gr.Textbox(label="Select Topic")
        submit2 = gr.Button("Submit")
        result2 = gr.Text()
        
    def submit_first_page(name, roll_no):
        return f"Name: {name}, Roll Number: {roll_no}", gr.update(visible=False), gr.update(visible=True)

# Function to handle the submission of the second page
    def submit_second_page(theme, topic):
        
        return f"Selected Theme: {theme}, Selected Topic: {topic}", gr.update(visible=False), gr.update(visible=True)
    
    submit1.click(fn=submit_first_page, inputs=[name, roll_no], outputs=[result1, page1, page2])
    page3 = create_third_page(data)
    submit2.click(fn=submit_second_page, inputs=[theme, topic], outputs=[result2, page2, page3])

demo.launch()


# Launch the Gradio app
demo.launch(share=True)


# def submit_second_page(theme, topic, data):
#         questionMaker = QuestionMaker(topic, theme)
#         userQuestions = questionMaker.get_questions(5)
#         new_data = []
#         for i in range(len(userQuestions)):
#             try:
#                 d = ast.literal_eval(userQuestions[i])
#                 new_data.append(d)
#             except Exception as e:
#                 print(f"Failed to write question {i+1}: {e}")
        
#         print(new_data)
#         return f"Selected Theme: {theme}, Selected Topic: {topic}", gr.update(visible=False), gr.update(visible=True)
