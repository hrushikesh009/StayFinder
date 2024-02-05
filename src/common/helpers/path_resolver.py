import os

import rootpath


class PathResolver:

    @staticmethod
    def get_absolute_path(file_path: str) -> str:

        abs_path = rootpath.detect()

        file_path = os.path.join(abs_path, file_path)
        return file_path

    @staticmethod
    def prepare_path(folder_path: str) -> str:
        full_path = rootpath.detect()

        full_path_list = full_path.split("/")
        folder_path_list = folder_path.split("/")

        if full_path_list[0] == folder_path_list[0]:
            new_folder_list = folder_path_list
            for full, folder in zip(full_path_list, folder_path_list):
                if full == folder:
                    new_folder_list = new_folder_list[1:]
                else:
                    raise Exception(f"Path to prepare is not part of the detected root path {full_path}")
            folder_path_list = new_folder_list

        for folder in folder_path_list:
            full_path = os.path.join(full_path, folder)
            if not os.path.exists(full_path):
                print(f"Preparing {full_path}")
                os.mkdir(full_path)

        return os.path.join(rootpath.detect(), folder_path)
