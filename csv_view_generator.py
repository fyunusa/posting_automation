
import shutil
from pathlib import Path
import os


class csv_view:
    def __init__(
        self,
        parent: str
    ) -> None:
        self.data_folder = parent

    
    def read_data_folder(self) -> list():
        data_list = os.listdir(self.data_folder)
        result = []
        for files in data_list:
            if files.endswith(".amr"):
                result.append(files)

        