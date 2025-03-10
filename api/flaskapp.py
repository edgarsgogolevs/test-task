import os
import logging
import traceback

from modules import setup_logger

lg = logging.getLogger()
setup_logger.init_log(lg)

from flask import Flask

app = Flask(__name__)

from modules.limiter import limiter

limiter.init_app(app)

from flask_cors import CORS

CORS(app)

# Register blueprints
from api.gemini import bp as gemini_bp

app.register_blueprint(gemini_bp)

from modules.swagger import init_swagger

init_swagger(app)


@app.route("/")
@limiter.exempt
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
  app.run(debug=True, port=int(os.getenv("PORT", 8080)))
