import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def login_data():
    return {
        "username": os.getenv("Username"),
        "password": os.getenv("Password")
    }

def auth_util():
    return os.getenv("Username"), os.getenv("Password")
