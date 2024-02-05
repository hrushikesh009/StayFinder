from marshmallow import Schema, fields
from src.model.response.hotel_search_simple_item_shema import \
    HotelSearchSimpleItemSchema


class HotelSearchResponseSchema(Schema):
    results = fields.Nested(HotelSearchSimpleItemSchema, many=True)

    @staticmethod
    def create_result_response(hotel_items_collection: dict):
        return {"results": hotel_items_collection}
