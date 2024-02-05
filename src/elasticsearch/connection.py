from elasticsearch_dsl import connections
from src.common.helpers.yaml_manager import YamlManager


class Connection:

    @staticmethod
    def create_connection() -> connections:
        hosts = YamlManager.read_yaml_content('parameters.yaml')['elasticsearch']['hosts']
        return connections.create_connection(hosts=hosts)
