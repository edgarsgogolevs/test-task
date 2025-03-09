from marshmallow import Schema, fields, EXCLUDE, validate

from modules.gemini import MODELS


class GeminiRequestSchema(Schema):

  class Meta:
    unknown = EXCLUDE

  query = fields.Str(required=True)
  model = fields.Str(validates=validate.OneOf(MODELS))

class GeminiGetModelsSchema(Schema):
  class Meta:
    unknown = EXCLUDE

  models = fields.List(fields.Str, required=True)
