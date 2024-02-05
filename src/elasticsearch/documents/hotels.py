from elasticsearch_dsl import Document, Join

HOTELS_INDEX = "hotels_index"


class Hotels(Document):
    class Index:
        name = HOTELS_INDEX
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    hotel_booking = Join(relations={"hotel": "booking"})

    @classmethod
    def _matches(cls, hit):
        # Hotels is an abstract class, make sure it never gets used for
        # deserialization
        return False

    def save(self, **kwargs):
        return super(Hotels, self).save(**kwargs)
