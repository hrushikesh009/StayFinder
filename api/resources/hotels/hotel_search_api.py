from flask import request
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask_restful import Resource, inputs, reqparse
from src.dependencies.hotel_search.query_builder import QueryBuilder
from src.dependencies.hotel_search.search_service import SearchService
from src.dependencies.hotel_search_criteria.hotel_search_criteria_director import \
    HotelSearchCriteriaDirector
from src.dependencies.hotel_search_criteria.hotel_search_criteria_url_builder import \
    HotelSearchCriteriaUrlBuilder
from src.model.request.hotel_search_request_shema import \
    HotelSearchRequestSchema  # noqa
from src.model.response.hotel_search_response_shema import \
    HotelSearchResponseSchema
from src.model.response.hotel_search_simple_item_shema import \
    HotelSearchSimpleItemSchema


class HotelSearchAPI(MethodResource, Resource):
    @doc(
        description='Search hotels API.',
        tags=['search'],
        params={
             "page": {
                 "description": "paging",
                 "in": "query",
                 "type": "int",
                 "default": 1,
                 "required": False
             },
             "size": {
                 "description": "size",
                 "in": "query",
                 "type": "int",
                 "default": 10,
                 "required": False
             },
             "n": {
                 "description": "hotel name",
                 "in": "query",
                 "type": "string",
                 "required": False
             },
             "c": {
                 "description": "city name",
                 "in": "query",
                 "type": "string",
                 "required": False
             },
             "lat": {
                 "description": "lat",
                 "in": "query",
                 "type": "float",
                 "required": False
             },
             "lng": {
                 "description": "lng",
                 "in": "query",
                 "type": "float",
                 "required": False
             },
             "fpn": {
                 "description": "free places",
                 "in": "query",
                 "type": "bool",
                 "required": False
             },
             "age": {
                 "description": "age",
                 "in": "query", "type":
                     "int", "default": 5,
                 "required": False
             }
        }
     )
    @doc(description='Search hotels API.', tags=['search'])

    def get(self):
        request_data = {
            "page": request.args.get('page', default = 1, type = int),
            "size": request.args.get('size', type=int, default=""),
            "n": request.args.get('n', type=str, default=""),
            "c": request.args.get('c', type=str, default=""),
            "lat": request.args.get('lat', type=float, default=""),
            "lng": request.args.get('lng', type=float, default=""),
            "fpn": request.args.get('fpn', type=inputs.boolean, default=""),
            "age": request.args.get('age', type=int, default="")
        }

        builder = HotelSearchCriteriaUrlBuilder(request_data)
        director = HotelSearchCriteriaDirector(builder)
        director.build_criteria()
        criteria = director.get_criteria()

        search_service = SearchService(QueryBuilder())
        search_results = search_service.search(criteria)

        hotel_items_collection = []

        for hotel in search_results:
            hotel_items_collection.append(
                HotelSearchSimpleItemSchema.create_item_from_es_response(hotel)
            )

        result_response = HotelSearchResponseSchema.create_result_response(
            hotel_items_collection
        )

        return result_response if request_data else 0, 200

    @staticmethod
    def prepareParser():
        parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        parser.add_argument('page', type=int, default="")
        parser.add_argument('size', type=int, default="")
        parser.add_argument('n', type=str, default="")
        parser.add_argument('c', type=str, default="")
        parser.add_argument('lat', type=float, default="")
        parser.add_argument('lng', type=float, default="")
        parser.add_argument('fpn', type=inputs.boolean, default="")
        parser.add_argument('age', type=int, default="")

        return parser