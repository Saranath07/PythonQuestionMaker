import gradio as gr
import os
import json
from app2 import create_third_page
import subprocess
from ..LangChain.main import QuestionMakersouce 

parent_directory = os.path.join('..', 'inputs')

if not os.path.exists(parent_directory):
    os.makedirs(parent_directory)

def save_data(theme, topic):
    data = {"theme": theme, "topic": topic}
    with open(os.path.join(parent_directory, "user_data.json"), "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    subprocess.run(["python3", "../LangChain/main.py"])
    return "Data saved successfully and main.py executed."

# Function to handle the submission of the first page
def submit_first_page(name, roll_no):
    return f"Name: {name}, Roll Number: {roll_no}", gr.update(visible=False), gr.update(visible=True)

# Function to handle the submission of the second page
def submit_second_page(theme, topic):
    save_data(theme, topic)
    return f"Selected Theme: {theme}, Selected Topic: {topic}", gr.update(visible=False), gr.update(visible=True)

# Create the Gradio interface
with gr.Blocks() as demo:
    # Page 1: User Details
    with gr.Column(visible=True) as page1:
        gr.Markdown("### Page 1: User Details")
        name = gr.Textbox(label="Name")
        roll_no = gr.Textbox(label="Roll Number")
        submit1 = gr.Button("Submit")
        result1 = gr.Text()
        
    # Page 2: Theme and Topic Selection
    with gr.Column(visible=False) as page2:
        gr.Markdown("### Page 2: Theme and Topic Selection")
        theme = gr.Textbox(label="Select theme")
        topic = gr.Textbox(label="Select Topic")
        submit2 = gr.Button("Submit")
        result2 = gr.Text()
        
    # Page 3: Final Page (imported from app2.py)

    # Setup the click actions
    submit1.click(fn=submit_first_page, inputs=[name, roll_no], outputs=[result1, page1, page2])
    page3 = create_third_page()
    submit2.click(fn=submit_second_page, inputs=[theme, topic], outputs=[result2, page2, page3])

# Launch the Gradio app
demo.launch(share=True)
