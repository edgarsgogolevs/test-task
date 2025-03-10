import os
import logging
from typing import Any, Generator

from google import genai

DEFAULT_MODEL = "gemini-2.0-flash"
MODELS = ("gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-pro")

lg = logging.getLogger("modules.gemini")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  lg.error("GEMINI_API_KEY is not set")
  raise Exception("GEMINI_API_KEY is not set")

try:
  client = genai.Client(api_key=api_key)
except Exception:
  lg.error("Failed to initialize Gemini client", exc_info=True)


def query_model(query: str, model: str = DEFAULT_MODEL) -> Generator[str | None, Any, Any]:
  """
    Query the Gemini model and yield the output as a stream of text/plain.
  """
  if model not in MODELS:
    lg.error(f"Model {model} not found")
    raise Exception(f"Model {model} not found")

  lg.info(f"Querying model {model} with query '{query}'")
  for chunk in client.models.generate_content_stream(model=model, contents=query):
    yield chunk.text
