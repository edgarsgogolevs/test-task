from flask import Blueprint, Response, jsonify
from flask_apispec import use_kwargs, marshal_with

from modules import gemini

from schemas.gemini import GeminiRequestSchema, GeminiGetModelsSchema


bp = Blueprint('gemini', __name__, url_prefix='/gemini')


@bp.route("/query", methods=["POST"])
@use_kwargs(GeminiRequestSchema)
def query_gemini(**kwargs):
  return Response(gemini.query_model(**kwargs), content_type="text/plain") # type: ignore


@bp.route("/models", methods=["GET"])
@marshal_with(GeminiGetModelsSchema)
def get_models():
  resp = {
    "models": gemini.MODELS
  }
  return jsonify(resp)
