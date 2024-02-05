from marshmallow import Schema, fields


class HotelSearchRequestSchema(Schema):
    page = fields.Int()
    size = fields.Int()
    n = fields.Str()
    c = fields.Str()
    lat = fields.Float()
    lng = fields.Float()
    fpn = fields.Bool()
    age = fields.Int()
