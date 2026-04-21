import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

# # Create the interface
# # inputs='text' specifies a textbox input
# # outputs='text' specifies a textbox output
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# # Launch the interface
# # The launch() method starts a local server
# # You can access the interface at the displayed URL
# demo.launch()


# def greet_with_age(name, age):
#     return f"Hello, {name}! You are {age} years old."

# # Inputs as a list: [textbox for name, number input for age]
# demo = gr.Interface(fn=greet_with_age, inputs=["text", "number"], outputs="text")

# demo.launch()


# def analyze_text(text):
#     word_count = len(text.split())
#     char_count = len(text)
#     return f"Word Count: {word_count}", f"Character Count: {char_count}"

# # Outputs as a list: [textbox for word count, textbox for character count]
# demo = gr.Interface(fn=analyze_text, inputs="text", outputs=["text", "text"])

# demo.launch()

# def echo_text(text):
#     return text

# demo_textbox = gr.Interface(
#     fn=echo_text,
#     inputs=gr.Textbox(label="Enter some text"),
#     outputs=gr.Textbox(label="Echoed text"),
#     title="Textbox Example"
# )

# demo_textbox.launch()

# def double_number(number):
#     return number * 2

# demo_number = gr.Interface(
#     fn=double_number,
#     inputs=gr.Number(label="Enter a number"),
#     outputs=gr.Number(label="Doubled number"),
#     title="Number Example"
# )

# demo_number.launch()

def add_ten(value):
    return value * 99.99

demo_slider = gr.Interface(
    fn=add_ten,
    inputs=gr.Slider(minimum=0, maximum=100, label="Select a value"),
    outputs=gr.Number(label="Value + 10"),
    title="Slider Example"
)
# demo_slider.launch()
def check_status(is_checked):
    return f"Checkbox is {'checked' if is_checked else 'unchecked'}"

demo_checkbox = gr.Interface(
    fn=check_status,
    inputs=gr.Checkbox(label="Check this box"),
    outputs=gr.Textbox(label="Status"),
    title="Checkbox Example"
)
# demo_checkbox.launch()

def show_choice(choice):
    return f"You selected: {choice}"

demo_dropdown = gr.Interface(
    fn=show_choice,
    inputs=gr.Dropdown(["Option A", "Option B", "Option C"], label="Choose an option"),
    outputs=gr.Textbox(label="Your choice"),
    title="Dropdown Example"
)

# demo_dropdown.launch()

def process_image(image):
    # In a real application, you would process the image here
    # For this example, we just return the image
    return image

demo_image = gr.Interface(
    fn=process_image,
    inputs=gr.Image(label="Upload an image"),
    outputs=gr.Image(label="Processed image"),
    title="Image Example"
)

demo_image.launch()