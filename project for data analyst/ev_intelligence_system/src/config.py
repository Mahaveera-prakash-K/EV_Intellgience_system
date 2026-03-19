import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

EV_API_URL = "https://data.wa.gov/resource/f6w7-q2d2.json"
DATA_FOLDER = "data"

# Sensitive YouTube API Key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")