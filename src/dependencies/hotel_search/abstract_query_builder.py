import abc

from elasticsearch_dsl import Search
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class AbstractQueryBuilder(abc.ABC):

    @abc.abstractmethod
    def create_query(self, criteria: HotelSearchCriteria):
        pass

    @abc.abstractmethod
    def get_search(self) -> Search:
        pass
