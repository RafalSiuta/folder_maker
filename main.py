from commands import Command
import flet
from flet import (
    FilePicker,
    ElevatedButton,
    Column,
    TextField,
    Page,
    colors
)
from widgets.card_widget import CardWidget
from menu import Menu

card = CardWidget()
#menu_option = Menu()
cmd = Command()

dial1 = FilePicker(on_result=cmd.create_default_folders)
dial3 = FilePicker(on_result=cmd.create_custom_folders)

names_list = TextField(label="Folder names or qty", hint_text="Add folder names... name1, name2, etc..")


def fun1():
    cmd.is_empty = False
    names_list.update()
    cmd.item_count = int(names_list.value)
    dial1.get_directory_path()


def fun2():
    cmd.is_empty = True
    names_list.update()
    cmd.item_count = int(names_list.value)
    dial1.get_directory_path()


def fun3():
    cmd.is_empty = False
    names_list.update()
    cmd.names_list = names_list.value
    print(cmd.names_list)
    dial3.get_directory_path()


def fun4():
    cmd.is_empty = True
    names_list.update()
    cmd.names_list = names_list.value
    print(cmd.names_list)
    dial3.get_directory_path()


def main(page: Page):
    # Pick files dialog
    page.window_bgcolor = colors.TRANSPARENT
    page.bgcolor = colors.BLACK54
    page.window_title_bar_hidden = False
    page.window_frameless = False
    page.window_left = 420
    page.window_top = 210
    page.window_max_width = 420
    page.window_max_height = 440
    page.window_width = 420
    page.window_height = 420

    page.overlay.extend([dial1, dial3,])

    page.add(
        Column(
            controls=[
                names_list,
                Column(
                    controls=[
                        ElevatedButton(text="Create default name empty folders ", on_click=lambda _:fun1()),
                        ElevatedButton(text="Create default name empty folders with note file",
                                       on_click=lambda _:fun2()),
                        ElevatedButton(text="Create custom name folders  ",
                                       on_click=lambda _: fun3()),
                        ElevatedButton(text="Create custom name folders with note file ",
                                       on_click=lambda _:fun4()),
                        ElevatedButton(text="Close app ",
                                       on_click=lambda _:print('close app')),

                    ]
                ),
            ]
        )

    )


flet.app(target=main)