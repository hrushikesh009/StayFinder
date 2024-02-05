from elasticsearch_dsl import Boolean, Float, GeoPoint, Integer, Nested, Text
from src.elasticsearch.documents.booking import Booking
from src.elasticsearch.documents.comment import Comment
from src.elasticsearch.documents.hotels import Hotels


class Hotel(Hotels):
    hotel_id = Integer()
    name = Text()
    city_name_en = Text()
    location = GeoPoint()
    age = Integer()
    free_places_at_now = Boolean()
    stars = Integer()
    rating = Float()
    comments = Nested(Comment)

    def add_comment(self, hotel_id, content, stars, created_at):
        c = Comment(hotel_id=hotel_id, content=content, stars=stars, created=created_at)
        self.comments.append(c)
        return c

    @classmethod
    def _matches(cls, hit):
        """ Use Booking class for parent documents """
        return hit["_source"]["hotel_booking"] == "hotel"

    @classmethod
    def search(cls, **kwargs):
        return cls._index.search(**kwargs).filter("term", hotel_booking="hotel")

    def add_booking(self, price, date, commit=True):
        booking = Booking(
            # required make sure the answer is stored in the same shard
            _routing=self.meta.id,
            # since we don't have explicit index, ensure same index as self
            _index=self.meta.index,
            # set up the parent/child mapping
            hotel_booking={"name": "booking", "parent": self.meta.id},
            # pass in the field values
            price=price,
            date=date
        )
        if commit:
            booking.save()
        return booking

    def search_bookings(self):
        # search only our index
        s = Booking.search()
        # filter for answers belonging to us
        s = s.filter("parent_id", type="hotel", id=self.meta.id)
        # add routing to only go to specific shard
        s = s.params(routing=self.meta.id)
        return s

    def get_bookings(self):
        """
        Get bookings either from inner_hits already present or by searching
        elasticsearch.
        """
        if "inner_hits" in self.meta and "booking" in self.meta.inner_hits:
            return self.meta.inner_hits.booking.hits
        return list(self.search_answers())

    def save(self, **kwargs):
        self.hotel_booking = "hotel"
        return super(Hotel, self).save(**kwargs)
