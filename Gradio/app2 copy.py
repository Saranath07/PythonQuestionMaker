import gradio as gr

# Read questions from a file
def get_questions():
    with open('questions.txt', 'r') as file:
        questions = file.readlines()
    return [q.strip() for q in questions]

questions = get_questions()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to execute the user's code
def run_code(code, question_index):
    question = questions[int(question_index)]
    
    try:
        # Prepare the global namespace for the execution
        exec_globals = {}
        exec(code, exec_globals)
        
        # Test the user's code with sample inputs and outputster
        if int(question_index) == 0:  # Example for adding two numbers
            result = exec_globals['add'](2, 3)  # Test case
            output = f"Output: {result}, Expected: 5"

        elif int(question_index) == 1:  # Example for checking prime
            is_prime = exec_globals.get('is_prime')
            if is_prime:
                result = exec_globals['is_prime'](5) # Test case with a prime number
                expected = True
                output = f"Output: {result}, Expected: {expected}"
            else:
                output = "Function 'is_prime' not found."

     
        elif int(question_index) == 2:  # Example for reversing a string
            result = exec_globals['reverse']("hello")  # Test case
            output = f"Output: {result}, Expected: 'olleh'"
        else:
            output = "No test case available for this question."
    except Exception as e:
        output = f"An error occurred: {str(e)}"
    
    return output
# Function to update the displayed question
def update_question_display(question_index):
    return questions[int(question_index)]

# Function to create the third page
def create_third_page():
    with gr.Column(visible=False) as page3:
        with gr.Row():
            question_dropdown = gr.Dropdown(choices=[str(i) for i in range(len(questions))], label="Select Question")
            question_display = gr.Textbox(label="Question", interactive=False)
        code_input = gr.Code(label="Write your code here", language="python")
        output_box = gr.Textbox(label="Output")
        run_button = gr.Button("Run")

        question_dropdown.change(fn=update_question_display, inputs=question_dropdown, outputs=question_display)
        run_button.click(fn=run_code, inputs=[code_input, question_dropdown], outputs=output_box)
    return page3

if __name__ == "__main__":
    app = gr.Blocks()
    create_third_page()
    app.launch()
