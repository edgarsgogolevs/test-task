import os
import logging
import traceback

from modules import setup_logger

lg = logging.getLogger()
setup_logger.init_log(lg)

from flask import Flask

app = Flask(__name__)

from flask_cors import CORS
CORS(app)

# Setup rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Limit by IP is used, realistically limit per user would be better.
limiter = Limiter(
  get_remote_address,
  app=app,
  default_limits=["200 per day", "50 per hour"],
  storage_uri="memory://",  # Memory storage used for simplicity, in real life use Redis or smth like that
)


@app.route("/")
def index_route():
  return "Hello from API!"


@app.errorhandler(500)
def server_error(_):
  lg.critical(traceback.format_exc())
  return {'error': 'Internal server error'}, 500


from api.gemini import bp as gemini_bp

app.register_blueprint(gemini_bp)

# run developement server
if __name__ == '__main__':
  # run debug app
  app.run(debug=True, port=int(os.getenv("PORT", 8080)))
