import os
import logging

from google import genai

MODEL = "gemini-2.0-flash"

lg = logging.getLogger("modules.gemini")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  lg.error("GEMINI_API_KEY is not set")
  raise Exception("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)
