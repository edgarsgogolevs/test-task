from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Limit by IP is used, realistically limit per user would be better.
limiter = Limiter(
  get_remote_address,
  default_limits=["200 per day", "50 per hour"],
  storage_uri="memory://",  # Memory storage used for simplicity, in real life use Redis or smth like that
)
