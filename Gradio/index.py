import gradio as gr
from app2 import create_third_page  # Import the function to create the third page

# Function to handle the submission of the first page
def submit_first_page(name, roll_no):
    return f"Name: {name}, Roll Number: {roll_no}", gr.update(visible=False), gr.update(visible=True)

# Function to handle the submission of the second page
def submit_second_page(theme, topic):
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
        theme = gr.Dropdown(label="Select Theme", choices=["Theme 1", "Theme 2", "Theme 3"])
        topic = gr.Dropdown(label="Select Topic", choices=["Topic A", "Topic B", "Topic C"])
        submit2 = gr.Button("Submit")
        result2 = gr.Text()
        
    # Page 3: Final Page (imported from app2.py)
    page3 = create_third_page()

    # Setup the click actions
    submit1.click(fn=submit_first_page, inputs=[name, roll_no], outputs=[result1, page1, page2])
    submit2.click(fn=submit_second_page, inputs=[theme, topic], outputs=[result2, page2, page3])

# Launch the Gradio app
demo.launch()
