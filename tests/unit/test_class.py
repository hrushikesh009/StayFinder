import json

from src.dependencies.hotel_search.query_builder import QueryBuilder
from src.dependencies.hotel_search.search_service import SearchService
from src.dependencies.hotel_search_criteria.hotel_search_criteria_director import \
    HotelSearchCriteriaDirector
from src.dependencies.hotel_search_criteria.hotel_search_criteria_url_builder import \
    HotelSearchCriteriaUrlBuilder
from src.model.response.hotel_search_simple_item_shema import \
    HotelSearchSimpleItemSchema


class TestClass:
    def test_one(self):
        request_data = {"c": "warsaw", "n": "golden", "age": 5, "lat": 52.21, "lng": 21.01}

        builder = HotelSearchCriteriaUrlBuilder(request_data)
        director = HotelSearchCriteriaDirector(builder)
        director.build_criteria()
        criteria = director.get_criteria()

        query_builder = QueryBuilder()
        query_builder.create_query(criteria)
        searh_query = query_builder.get_search()

        search_service = SearchService(QueryBuilder())
        search_results = search_service.search(criteria)

        for hotel in search_results:
            item = HotelSearchSimpleItemSchema.create_item_from_es_response(hotel)
            assert item['star'] == 5

