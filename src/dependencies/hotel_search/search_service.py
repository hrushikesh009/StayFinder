from src.dependencies.hotel_search.abstract_query_builder import \
    AbstractQueryBuilder
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class SearchService():

    def __init__(self, builder: AbstractQueryBuilder):
        self.builder = builder

    def search(self, criteria: HotelSearchCriteria):
        self.builder.create_query(criteria)
        search = self.builder.get_search()

        return search.execute()
