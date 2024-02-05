from elasticsearch_dsl import Q, Search
from src.dependencies.hotel_search.abstract_query_builder import \
    AbstractQueryBuilder
from src.dependencies.hotel_search.filters.city_name_filter import \
    CityNameFilter
from src.dependencies.hotel_search.filters.geo_distance_filter import \
    GeoDistanceFilter
from src.dependencies.hotel_search.filters.hotel_name_filter import \
    HotelNameFilter
from src.dependencies.hotel_search.filters.hotel_range_age_filter import \
    HotelRangeAgeFilter
from src.elasticsearch.connection import Connection
from src.elasticsearch.documents.hotels import HOTELS_INDEX
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class QueryBuilder(AbstractQueryBuilder):

    def __init__(self):
        self.search = Search(using=Connection.create_connection(), index=HOTELS_INDEX)

    def get_search(self) -> Search:
        return self.search

    def create_query(self, criteria: HotelSearchCriteria):
        self.set_page_offset(criteria)
        self.set_fields(criteria)
        self.set_filters(criteria)
        self.set_sorting(criteria)
        self.set_aggregations(criteria)

    def set_filters(self, criteria: HotelSearchCriteria):
        must_conditions = []
        should_conditions = []
        filter_conditions = []

        if criteria.city_name:
            must_conditions.append(CityNameFilter.create_filter(criteria))

        if criteria.hotel_name:
            must_conditions.append(HotelNameFilter.create_filter(criteria))

        if criteria.hotel_age:
            should_conditions.append(HotelRangeAgeFilter.create_filter(criteria))

        if criteria.geo_coordinates:
            filter_conditions.append(GeoDistanceFilter.create_filter(criteria))

        q_res = Q('bool', must=must_conditions, should=should_conditions, filter=filter_conditions)

        self.search = self.search.query(q_res)

    def set_page_offset(self, criteria: HotelSearchCriteria):
        start_from = (criteria.page - 1) * criteria.size
        start_from = start_from if start_from >= 0 else 0
        self.search = self.search[start_from:criteria.size]

    def set_fields(self, criteria: HotelSearchCriteria):
        # choose fields you want to get from ElasticSearch
        pass

    def set_aggregations(self, criteria: HotelSearchCriteria):
        # add aggregations
        pass

    def set_sorting(self, criteria: HotelSearchCriteria):
        # add sorting
        pass
