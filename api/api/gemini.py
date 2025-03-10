from flask import Blueprint, Response, jsonify
from flask_apispec import use_kwargs, marshal_with

from modules import gemini
from modules.limiter import limiter

from schemas.gemini import GeminiQueryRequestSchema, GeminiGetModelsSchema


bp = Blueprint('gemini', __name__, url_prefix='/gemini')


@bp.route("/query", methods=["POST"])
@use_kwargs(GeminiQueryRequestSchema)
@marshal_with(None, code="200", description="Returns a model output as a stream of text/plain")
def query_gemini(**kwargs):
  return Response(gemini.query_model(**kwargs), content_type="text/plain") # type: ignore


@bp.route("/models", methods=["GET"])
@marshal_with(GeminiGetModelsSchema, code="200")
@limiter.exempt
def get_models():
  resp = {
    "models": gemini.MODELS
  }
  return jsonify(resp), 200
