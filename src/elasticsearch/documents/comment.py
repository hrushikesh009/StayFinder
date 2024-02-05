from elasticsearch_dsl import Date, InnerDoc, Integer, Text


class Comment(InnerDoc):
    hotel_id = Integer()
    content = Text()
    stars = Integer()
    created_at = Date()
