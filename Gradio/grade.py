import gradio as gr

def calculate_grade(marks):
    try:
        marks = float(marks)
        if 90 <= marks <= 100:
            return "S"
        elif 80 <= marks < 90:
            return "A"
        elif 70 <= marks < 80:
            return "B"
        elif 60 <= marks < 70:
            return "C"
        elif 50 <= marks < 60:
            return "D"
        elif 40 <= marks < 50:
            return "E"
        elif 0 <= marks < 40:
            return "Fail"
        else:
            return "Invalid marks. Please enter a number between 0 and 100."
    except ValueError:
        return "Invalid input. Please enter a valid input"

# Create the Gradio interface
demo = gr.Interface(
    fn=calculate_grade,
    # inputs=gr.Textbox(label="Enter Marks"),
    inputs = gr.Textbox(label = "Marks"),
    outputs=gr.Textbox(label="Grade"),
    title="Student Grade Calculator",
    description="Enter the marks to calculate the grade based on the given scheme.",
    live = True
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
