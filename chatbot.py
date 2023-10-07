import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import openai

# Initialize OpenAI API key
openai.api_key = ""

# Initial system message
system_message ="You are an AI chatbot powered by Alibaba Cloud, specialized in crafting optimal cloud solutions tailored to users specific needs. Your mission is to aid users in determining the ideal configuration that aligns seamlessly with their requirements within Alibaba Cloud’s extensive range of solutions. To accurately discern user needs, you need to initiate the conversation by posing at least 10 pertinent questions related to cloud specifications and requirements, ensuring a comprehensive understanding of their expectations. One question should specifically inquire about the preferred region, for instance, Riyadh, to ensure optimal performance and regulatory compliance. Upon receiving responses to all your queries, assess the users needs meticulously and propose a suitable Alibaba Cloud solution that may encompass elements like VPC, vSwitch, Auto Scaling, ALB, and Security Group, adjusted to their unique demands. If needed, include Auto Scaling in the Security Group and elucidate which ports are permitted.Present the requirements as concise, clear points without extended explanations and wait for user responses before suggesting any solutions. After users review the proposed solution, await their approval before generating a customized Terraform  template with  all Configure  propertiesfor their use. Subsequently, verify with users if the provided solution meets their expectations or necessitates any modifications. Please maintain your focus on addressing Alibaba Cloud-related inquiries exclusively and refrain from providing solutions or responses until the user expresses their preference or ideas.Start by confirming if users are ready to proceed with the questions, information, curate an Alibaba Cloud solution that meticulously aligns with their requirements and present it for their approval. After acquiring their consent, create a precise Terraform template and confirm if it suffices or if further adjustments are necessary. Ensure all your interactions and responses are strictly confined to Alibaba Cloud-related discussions and await user prompts before making any suggestions or providing information."

# Function to handle sending user message and receiving bot response
def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        # Display user message in the chat window
        chat_window.insert(tk.END, "You: " + user_message + "\n\n")
        
        # Reset the user input field
        user_input.delete("1.0", tk.END)

        # Prepare the message for OpenAI (including the system message)
        messages = [{"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}]
        
        # Get bot's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Get bot's reply from the response
        bot_reply = response['choices'][0]['message']['content']

        # Display bot's reply in the chat window
        chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")

# Function to handle quitting the application
def quit_application():
    if messagebox.askokcancel("Quit", "Do you want to quit the chatbot?"):
        root.destroy()

# Initialize the GUI
root = tk.Tk()
root.title("Alibaba Cloud Chatbot")
root.geometry("700x700")

# Create an input field for the user
user_input = tk.Text(root, width=40, height=5)
user_input.pack(padx=10, pady=10)

# Create a scrolled text widget for the chat window
chat_window = scrolledtext.ScrolledText(root, width=50, height=50)
chat_window.pack(padx=10, pady=10)

# Create a "Send" button to send the user's message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Bind the "Enter" key to send the user's message
root.bind('<Return>', lambda event: send_message())

# Create a menu bar with a "Quit" option
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=quit_application)

# Start the GUI main loop
root.mainloop()
