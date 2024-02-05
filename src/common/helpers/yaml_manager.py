import sys

import yaml
from src.common.helpers.path_resolver import PathResolver


class YamlManager:

    @staticmethod
    def read_yaml_content(file_name: str, *args, **kwargs):
        try:
            with open(PathResolver.get_absolute_path(file_name)) as stream:
                content = yaml.load(stream, Loader=yaml.Loader, *args, **kwargs)
        except Exception as e:
            print("YamlManager: Could not load yaml file from path: " + file_name)
            print(e)
            sys.exit()

        return content

    @staticmethod
    def save_in_yaml(dict_to_save: dict, file_name: str, *args, **kwargs):
        try:
            with open(PathResolver.get_absolute_path(file_name), 'w') as outfile:
                yaml.dump(dict_to_save, outfile, *args, **kwargs)
        except Exception as e:
            print("YamlManager: Could not save yaml file: " + file_name)
            print(e)
            sys.exit()
