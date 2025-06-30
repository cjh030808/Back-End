from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
