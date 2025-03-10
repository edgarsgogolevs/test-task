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

# Register blueprints
from api.gemini import bp as gemini_bp

app.register_blueprint(gemini_bp)

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

from flask_apispec.extension import FlaskApiSpec  # type: ignore
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from apispec import APISpec

app.config.update({
  "APISPEC_SPEC":
    APISpec(
      title="Numbero Test API",
      version="v1",
      openapi_version="2.0",
      plugins=[MarshmallowPlugin()],
    ),
  "APISPEC_SWAGGER_URL":
    "/swagger/",
  "APISPEC_SWAGGER_UI_URL":
    "/swagger-ui/",
})

docs = FlaskApiSpec(app)
docs.register_existing_resources()


@app.route("/")
def index_route():
  return "Hello from API!"


@app.errorhandler(404)
def pageNotFound(error):
  lg.warning(f"404 {error}")
  return {"error": "Not found"}, 404


@app.errorhandler(500)
def server_error(_):
  lg.critical(traceback.format_exc())
  return {'error': 'Internal server error'}, 500


# run developement server
if __name__ == '__main__':
  # run debug app
  app.run(debug=True, port=int(os.getenv("PORT", 8080)))
