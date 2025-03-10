from flask_apispec.extension import FlaskApiSpec  # type: ignore
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from apispec import APISpec
from flask import Flask


def init_swagger(app: Flask):
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
