import os
from pathlib import Path


class InputFile:

    def __init__(self, file_name: str = None):
        parent = str(Path(__file__).parent)

        if file_name:
            self.path = os.path.abspath(f'{parent}/{file_name}')
        else:
            self.path = InputFile.get_current_folder()

    @staticmethod
    def get_current_folder() -> str:
        return str(Path(__file__).parent)

    def __str__(self) -> str:
        return self.path
