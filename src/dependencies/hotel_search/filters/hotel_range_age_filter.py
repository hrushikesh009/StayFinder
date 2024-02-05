from elasticsearch_dsl import Q
from src.dependencies.hotel_search.filters.abstract_filter import \
    AbstractFilter
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class HotelRangeAgeFilter(AbstractFilter):
    @staticmethod
    def create_filter(criteria: HotelSearchCriteria) -> Q:
        q_res = Q("range", age={"gte": criteria.hotel_age})

        return q_res
