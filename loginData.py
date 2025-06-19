import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Function to retrieve login data from environment variables
def login_data(): #used for giving json data to the API
    return {
        "username": os.getenv("Username"),
        "password": os.getenv("Password")
    }

def auth_util(): #used for giving auth data to the API
    return os.getenv("Username"), os.getenv("Password")
