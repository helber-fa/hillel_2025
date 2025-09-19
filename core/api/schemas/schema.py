from marshmallow import Schema, fields

class UserSchema(Schema):
    userId = fields.Integer(required=True)
    distanceUnits = fields.Str(required=True)
    currency = fields.Str(required=True)
    photoFilename = fields.Str(required=True)

class CurrentSchema(Schema):
    status = fields.Str(required=True)
    data = fields.Nested(UserSchema, required=True)

response = {
"status": "ok",
"data": {
    "distanceUnits": "km",
    "userId": 1,
    "currency": "True",
    "photoFilename": "default-user.png"
  }
}

CurrentSchema().load(response)



