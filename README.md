# Animals Website Generator

This project generates a simple HTML website with information about animals.
The data is fetched from an external API based on user input.

The user enters an animal name, and the program retrieves data from the API
and displays the results on a generated webpage.

---

## Installation

1. Clone the repository
2. Install dependencies:

#bash
#pip install -r requirements.txt

#Create a .env file and add:
API_KEY=your_api_key_here


#Run the program:

python animals_web_generator.py


#Enter an animal name when prompted:

#Please enter an animal: Fox


#An HTML file called animals.html will be generated.

#Project Structure
.
#├── animals_web_generator.py
#├── data_fetcher.py
#├── requirements.txt
#├── .gitignore
#└── README.md