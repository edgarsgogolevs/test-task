from marshmallow import Schema, fields, EXCLUDE, validate

from modules.gemini import MODELS


class GeminiQueryRequestSchema(Schema):

  class Meta:
    unknown = EXCLUDE

  query = fields.Str(required=True, validate=validate.Length(min=5, max=5120))
  model = fields.Str(validate=validate.OneOf(MODELS))

class GeminiGetModelsSchema(Schema):
  class Meta:
    unknown = EXCLUDE

  models = fields.List(fields.Str, required=True)
