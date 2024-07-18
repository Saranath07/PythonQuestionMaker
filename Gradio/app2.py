import gradio as gr
import json
import os

# Define the parent directory for the templates
template_directory = os.path.join('..', 'json_files')

# Function to read a JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to load template based on selection
def load_template(template_name):
    file_path = os.path.join(template_directory, f"{template_name}.json")
    if os.path.exists(file_path):
        return read_json_file(file_path)
    else:
        return {"problem_statement": "", "function_template": "", "test_cases": [], "function_name": ""}

# Function to run the user code
def run_code(code, template_name):
    data = load_template(template_name)
    outputs = []
    try:
        function_name = data["function_name"]
        exec_globals = {}
        exec(code, exec_globals)
        func = exec_globals.get(function_name)
        
        if not func:
            return [f"Function '{function_name}' not found."] * len(data["test_cases"])

        for test_case in data["test_cases"]:
            inputs = list(map(int, test_case["input"].split(", ")))
            expected_output = int(test_case["output"])
            result = func(*inputs)
            output = f"Input: {test_case['input']}\nOutput: {result}, Expected: {expected_output}"
            outputs.append(output)
    except Exception as e:
        outputs = [f"An error occurred: {str(e)}"] * len(data["test_cases"])
    
    return outputs

def create_third_page():
    def load_and_display_template(template_name):
        template_data = load_template(template_name)
        question_display.update(value=template_data["problem_statement"])
        code_input.update(value=template_data["function_template"].replace("\\n", "\n"))
        for i, test_case in enumerate(template_data["test_cases"]):
            input_boxes[i].update(value=test_case['input'])
            output_boxes[i].update(value="")
        return template_data

    with gr.Column(visible=False) as page3:
        template_selector = gr.Dropdown(label="Select a template", choices=["template_1", "template_2"], value="template_1")
        template_selector.change(fn=load_and_display_template, inputs=template_selector, outputs=None)
        
        question_display = gr.Textbox(label="Question", value="", interactive=False)
        code_input = gr.Code(label="Write your code here", language="python", value="")

        input_boxes = [gr.Textbox(label=f"Input for Test Case {i+1}", value="", interactive=False) for i in range(2)]
        output_boxes = [gr.Textbox(label=f"Output for Test Case {i+1}") for i in range(2)]

        run_button = gr.Button("Run")
        run_button.click(fn=run_code, inputs=[code_input, template_selector], outputs=output_boxes)
    
    return page3
