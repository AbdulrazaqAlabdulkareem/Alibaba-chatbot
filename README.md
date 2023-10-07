# Alibaba Cloud Chatbot

This chatbot interacts with users in a conversational manner to assist them in configuring Alibaba Cloud solutions and generating Terraform templates for deployment.

## Prerequisites

- Python 3.x
- tkinter library (should be included in most standard Python installations)
- An OpenAI API key (provide the key in the `openai.api_key` variable)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdulrazaqAlabdulkareem/Alibaba-chatbot.git
    cd Alibaba-chatbot
    ```

2. Install the required Python libraries:
    ```bash
    pip install openai
    ```

3. Set up your OpenAI API key by replacing `openai.api_key` with your actual API key in the code.

## Usage

1. Run the chatbot script:
    ```bash
    python chatbot.py
    ```

2. The chatbot GUI will open. Follow the prompts to provide deployment ideas and answer 10 questions related to Alibaba Cloud solutions.

3. The chatbot will generate an Alibaba Cloud solution based on the provided information.

4. Review and approve the proposed solution.

5. The chatbot will generate a Terraform template for the approved solution, which you can use for deployment.

## Features

- The chatbot initiates conversations with a system message outlining its capabilities and instructions to the user.
- It gathers deployment ideas and asks 10 questions related to Alibaba Cloud solutions.
- It uses OpenAI GPT-3.5 Turbo to generate responses based on user input.
- The conversation history is displayed in the chat window, showing both user and bot messages.

## Configuration

- Update the `system_message` variable to customize the introductory system message.
- Modify the conversation flow, questions, or responses as needed.

## Contributing

Contributions are welcome! Feel free to open issues or create pull requests to improve the chatbot.

## License

This project is licensed under the MIT License.
