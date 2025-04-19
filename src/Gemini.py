# Import the Google module for the API
from google import genai  # Import the genai module for the API
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


class Gemini:
    def __init__(self):
        configure()
        self.client = genai.Client(api_key=os.getenv('api_key'))
        self.model = "gemini-2.0-flash"
        self.name = "Gemini"  # Initialize name
        self.symbol = ""      # Initialize symbol

    def get_details(self) -> str:
        return f"Gemini Name: {self.name}, Symbol: {self.symbol}"

    def update_symbol(self, new_symbol: str):
        self.symbol = new_symbol

    def generate_response(self, prompt) -> str:
        """
        Generate a response using the Gemini API.
        """
        response = self.client.models.generate_content(model=self.model, contents=prompt)
        return response.text or ""