import src.elasticsearch.documents as documents
from elasticsearch_dsl import Date, Float


class Booking(documents.Hotels):
    price = Float()
    date = Date()

    @classmethod
    def _matches(cls, hit):
        """ Use Booking class for child documents with child name 'booking' """
        return (
                isinstance(hit["_source"]["hotel_booking"], dict)
                and hit["_source"]["hotel_booking"].get("name") == "booking"
        )

    @classmethod
    def search(cls, **kwargs):
        return cls._index.search(**kwargs).exclude("term", hotel_booking="hotel")

    @property
    def hotel(self):
        # cache hotel in self.meta
        # any attributes set on self would be interpretted as fields
        if "hotel" not in self.meta:
            self.meta.hotel = documents.Hotel.get(
                id=self.hotel_booking.parent, index=self.meta.index
            )
        return self.meta.hotel

    def save(self, **kwargs):
        # set routing to parents id automatically
        self.meta.routing = self.hotel_booking.parent
        return super(Booking, self).save(**kwargs)
