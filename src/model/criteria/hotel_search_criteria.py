class HotelSearchCriteria():
    DEFAULT_PAGE = 1
    DEFAULT_SIZE = 10
    SIZE_MIN = 1
    SIZE_MAX = 20

    def __init__(self):
        self._page = self.DEFAULT_PAGE
        self._size = self.DEFAULT_SIZE
        self._free_places_at_now = False
        self._hotel_name = None
        self._city_name = None
        self._hotel_age = None
        self._hotel_stars = None
        self._geo_coordinates = None

    @property
    def page(self) -> int:
        return self._page

    @page.setter
    def page(self, value: int):
        self._page = value

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    @property
    def free_places_at_now(self) -> bool:
        return self._free_places_at_now

    @free_places_at_now.setter
    def free_places_at_now(self, value: bool):
        self._free_places_at_now = value

    @property
    def hotel_name(self) -> str:
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value: str):
        self._hotel_name = value

    @property
    def city_name(self) -> str:
        return self._city_name

    @city_name.setter
    def city_name(self, value: str):
        self._city_name = value

    @property
    def hotel_age(self) -> int:
        return self._hotel_age

    @hotel_age.setter
    def hotel_age(self, value: int):
        self._hotel_age = value

    @property
    def hotel_stars(self) -> int:
        return self._hotel_stars

    @hotel_stars.setter
    def hotel_stars(self, value: int):
        self._hotel_stars = value

    @property
    def geo_coordinates(self) -> dict:
        return self._geo_coordinates

    @geo_coordinates.setter
    def geo_coordinates(self, value: dict):
        self._geo_coordinates = value
