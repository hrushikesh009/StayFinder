from src.dependencies.hotel_search_criteria.abstract_criteria_builder import \
    AbstractCriteriaBuilder
from src.dependencies.hotel_search_criteria.abstract_criteria_director import \
    AbstractCriteriaDirector
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria


class HotelSearchCriteriaDirector(AbstractCriteriaDirector):
    def __init__(self, builder: AbstractCriteriaBuilder):
        self.builder = builder

    def build_criteria(self):
        self.builder.create_criteria()

    def get_criteria(self) -> HotelSearchCriteria:
        return self.builder.get_criteria()
