import subprocess
import datetime
import shutil
import os
from flet import (
    FilePickerResultEvent,
)


class Command:

    def __init__(self):
        self.date = datetime.datetime.now()
        self.user_path = os.path.expanduser("~")
        self.names_list = ''
        self.is_empty = True
        self.item_count = 0

    @staticmethod
    def command(name):
        return f"mkdir {name}"

    @staticmethod
    def copy_file(path):
        current_path = 'static/files/note.pages'
        shutil.copyfile(current_path, path)

    def subprocess(self, folder_name, directory_path):
        subprocess.run([self.command(folder_name)], shell=True, capture_output=True,
                       cwd=directory_path)

    def open_finder(self, path):
        subprocess.run([f'open /{path}'], shell=True, capture_output=True,
                       cwd=path)

    def create_default_folders(self, e: FilePickerResultEvent):
        #folder_count = 3  # int(input("How many folders? "))

        if e.path:
            for num in range(1, self.item_count + 1):
                folder_name = f'{num}{self.date.strftime("%a%d%b%y")}'
                try:
                    self.subprocess(folder_name, e.path)
                    # self.open_finder(e.path)

                    if self.is_empty:
                        self.copy_file(f"{e.path}/{folder_name}/note{num}.pages")

                except FileExistsError as ex:
                    print(f"error: /n {ex}")

        else:
            print("Cancelled!")

    def create_custom_folders(self, e: FilePickerResultEvent):

        if e.path:
            names = self.names_list.split(',')

            for name in names:
                try:
                    self.subprocess(name, e.path)

                    if self.is_empty:
                        self.copy_file(f"{e.path}/{name}/{name}.pages")

                except FileExistsError as ex:
                    print(f"error: /n {ex}")
        else:
            print('Cancelled')