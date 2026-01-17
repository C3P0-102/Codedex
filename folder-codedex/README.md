📝 Blog Generation

This project is a simple command-line blog/paragraph generator built using Python and the OpenAI API. It allows users to generate short paragraphs on any topic by providing a prompt in the terminal.

<iframe src="https://assets.pinterest.com/ext/embed.html?id=311311393010400413" align="center" height="281" width="236" frameborder="0" scrolling="no" ></iframe>

🚀 Features

Generates a paragraph on any given topic

Uses OpenAI’s gpt-3.5-turbo-instruct model

Secure API key handling with .env

Interactive CLI-based input

Adjustable creativity via temperature control

🛠️ Tech Stack

Python

OpenAI Python SDK

python-dotenv

📦 Installation

Clone the repository

git clone <your-repo-url>
cd <repo-folder>


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies

pip install openai python-dotenv

🔐 Environment Setup

Create a .env file in the root directory and add your OpenAI API key:

API_KEY=your_openai_api_key_here


⚠️ Never commit your .env file to GitHub.

▶️ How to Run
python main.py


You’ll be prompted with:

Write a paragraph? Y for yes, anything else for no.


Enter Y to generate a paragraph

Enter the topic when asked

Any other input exits the program

⚙️ How It Works

Reads the OpenAI API key securely from .env

Sends the topic as a prompt to OpenAI

Receives and prints a generated paragraph

Loops until the user chooses to stop

🧠 Customization

You can tweak:

max_tokens → Control paragraph length

temperature → Control creativity (lower = more factual)

📌 Notes

Requires an active OpenAI API key

Internet connection needed

Designed for learning and experimentation

📄 License

This project is open-source and free to use for educational purposes.
