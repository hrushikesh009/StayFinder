from elasticsearch_dsl import Q
from src.dependencies.hotel_search.filters.abstract_filter import \
    AbstractFilter
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class GeoDistanceFilter(AbstractFilter):
    DISTANCE = "30km"

    @staticmethod
    def create_filter(criteria: HotelSearchCriteria) -> Q:
        q_res = Q("geo_distance", location=criteria.geo_coordinates, distance=GeoDistanceFilter.DISTANCE)

        return q_res
