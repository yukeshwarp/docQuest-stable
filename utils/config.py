import os
from dotenv import load_dotenv

load_dotenv()

azure_endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("API_KEY")
api_version = os.getenv("API_VERSION")
model = os.getenv("MODEL")
azure_function_url = os.getenv("AZURE_FUNCTION_URL")
