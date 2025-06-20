# simple_chatbot_for_reccomendation
## How to Run the App

1. **Clone the repository**  
   ```bash
   git clone https://github.com/aframahendrap/simple_chatbot_for_reccomendation.git

2. **Change into this directory**
    ```bash
   cd simple_chatbot_for_reccomendation
4. **Create and activate the virtual environment**
    ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
5. **Set the .env file or you can copy the .env file in this repository**
6. **Install depedencies**
    ```bash
   pip install -r requirements.txt
7. **Run the main.py file**
   ```bash
   uvicorn main:app --reload
8. **Open the FASTAPI app using your browser**
   ```bash
   http://127.0.0.1:8000/docs
