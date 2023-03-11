from marshmallow import Schema, fields


class RequestSchema(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)
