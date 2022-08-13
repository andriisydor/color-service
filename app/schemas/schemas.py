from marshmallow import Schema, fields


class ColorSchema(Schema):
    id = fields.Int()
    red = fields.Int()
    green = fields.Int()
    blue = fields.Int()


class PaletteSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    date = fields.Date()
    colors = fields.List(fields.Nested(ColorSchema))
