from datetime import datetime

import click
from src.elasticsearch.connection import Connection
from src.elasticsearch.documents.booking import Booking
from src.elasticsearch.documents.hotel import Hotel
from src.elasticsearch.documents.hotels import Hotels


class FillElasticsearch:
    @staticmethod
    @click.command("fill-elasticsearch")
    def run():
        click.secho('Saving data to elasticsearch')
        FillElasticsearch.fill_elasticsearch()
        click.secho('Done.')

    @staticmethod
    def fill_elasticsearch():
        # create connection to elasticsearch
        Connection.create_connection()

        # create the mappings in elasticsearch
        Hotels.init()
        Hotel.init()
        Booking.init()

        hotel = Hotel(
            _id=1,
            hotel_id=1,
            name="Golden star hotel",
            city_name_en="Warsaw",
            location={"lat": "52.21", "lon": "21.01"},
            age=7,
            stars=5,
            free_places_at_now=True,
            rating=4.85
        )

        hotel.add_comment(
            hotel_id=1,
            stars=5,
            content="Some content",
            created_at=datetime.now()
        )

        hotel.save()

        hotel.add_booking(200, datetime.now())

        hotel = Hotel(
            _id=2,
            hotel_id=2,
            name="Silver star hotel",
            city_name_en="Warsaw",
            location={"lat": "52.13", "lon": "21.01"},
            age=7,
            stars=4,
            free_places_at_now=True,
            rating=4.6
        )

        hotel.save()


if __name__ == '__main__':
    FillElasticsearch.run()
