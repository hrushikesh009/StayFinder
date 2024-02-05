from src.dependencies.hotel_search_criteria.abstract_criteria_builder import \
    AbstractCriteriaBuilder
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria

PAGE = 'page'
SIZE = 'size'
HOTEL_NAME = "n"
HOTEL_CITY_NAME_EN = "c"
CITY_CENTER_LAT = "lat"
CITY_CENTER_LNG = "lng"
HOTEL_STARS = "stars"
HOTEL_FREE_PLACES = "fpn"
HOTEL_AGE = "age"


class HotelSearchCriteriaUrlBuilder(AbstractCriteriaBuilder):
    def __init__(self, data: dict):
        self.data = data
        self.criteria = HotelSearchCriteria()

    def create_criteria(self):
        if PAGE in self.data and isinstance(self.data[PAGE], int):
            self.criteria.page = self.data[PAGE]

        if SIZE in self.data and isinstance(self.data[SIZE], int) and self.data[SIZE] <= HotelSearchCriteria.SIZE_MAX:
            self.criteria.size = self.data[SIZE]

        if HOTEL_AGE in self.data and isinstance(self.data[HOTEL_AGE], int):
            self.criteria.hotel_age = self.data[HOTEL_AGE]

        if HOTEL_STARS in self.data and isinstance(self.data[HOTEL_STARS], int):
            self.criteria.hotel_stars = self.data[HOTEL_STARS]

        if HOTEL_NAME in self.data and isinstance(self.data[HOTEL_NAME], str):
            self.criteria.hotel_name = self.data[HOTEL_NAME]

        if HOTEL_CITY_NAME_EN in self.data and isinstance(self.data[HOTEL_CITY_NAME_EN], str):
            self.criteria.city_name = self.data[HOTEL_CITY_NAME_EN]

        if HOTEL_FREE_PLACES in self.data and isinstance(self.data[HOTEL_FREE_PLACES], bool):
            self.criteria.free_places_at_now = self.data[HOTEL_FREE_PLACES]

        if (
                CITY_CENTER_LAT in self.data and isinstance(self.data[CITY_CENTER_LAT], float) and
                CITY_CENTER_LNG in self.data and isinstance(self.data[CITY_CENTER_LNG], float)
        ):
            self.criteria.geo_coordinates = {"lat": self.data[CITY_CENTER_LAT], "lon": self.data[CITY_CENTER_LNG]}

    def get_criteria(self) -> HotelSearchCriteria:
        return self.criteria
