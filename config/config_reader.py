import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('QA_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
BROWSER = os.getenv('BROWSER')
HEADLESS = os.getenv('HEADLESS',"False").lower() == "true"