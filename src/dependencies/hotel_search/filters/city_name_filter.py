from elasticsearch_dsl import Q
from src.dependencies.hotel_search.filters.abstract_filter import \
    AbstractFilter
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class CityNameFilter(AbstractFilter):
    FUZZINESS = 2

    @staticmethod
    def create_filter(criteria: HotelSearchCriteria) -> Q:
        q1 = Q("match", city_name_en={"query": criteria.city_name, "fuzziness": CityNameFilter.FUZZINESS})
        q2 = Q("match", city_name_en={"query": "London"})
        q_res = Q('bool', should=[q1, q2])

        return q_res
