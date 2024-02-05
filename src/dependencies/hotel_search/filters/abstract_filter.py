import abc

from elasticsearch_dsl import Q
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class AbstractFilter(abc.ABC):

    @abc.abstractstaticmethod
    def create_filter(self, criteria: HotelSearchCriteria) -> Q:
        pass
