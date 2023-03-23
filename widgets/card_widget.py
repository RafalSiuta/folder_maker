from flet import (ElevatedButton, FilePicker)
from commands import Command
from menu import Menu


class CardWidget:

    def __init__(self):
        self.dialog = FilePicker()

    def action_handler(self, opt_id):
        cmd = Command()
        if opt_id == 1:
              self.dialog = FilePicker(on_result=cmd.create_default_folders)
        elif opt_id == 2:
              self.dialog.on_result(print('test function 2'))
        elif opt_id == 3:
              self.dialog.on_result(print('test function 3'))
        elif opt_id == 4:
              self.dialog.on_result(print('test function 4'))
        elif opt_id == 5:
              self.dialog.on_result(print('test function 5'))
        return self.dialog.get_directory_path()

    def card(self):
        buttons = []
        menu_option = Menu()
        for opt in menu_option.options():
            # if opt['id'] == 1:
            #     opt['click'] = cmd.create_default_folders
            # elif opt['id'] == 2:
            #     opt['click'] = print('test function 2')
            # elif opt['id'] == 3:
            #     opt['click'] = print('test function 2'
            # elif opt['id'] == 4:
            #     opt['click'] = print('test function 2')
            # elif opt['id'] == 5:
            #     opt['click'] = print('test function 2')
            # dialog = self.dialog.on_result(opt['click'])
            buttons.append(ElevatedButton(text=opt['opt'], on_click=lambda _: self.action_handler(opt['id'])))

        return buttons
#Grafika_warsztatowa,Typografia_Projekt,ProjSysIdenWiz,WarKomputerowy,KreaRozwPodm,ProjGrafMultimed,MulTechCyf,StrukWiz,SztuPopHisGraf,Ang,DigPaint,Fotog,GrafWyd