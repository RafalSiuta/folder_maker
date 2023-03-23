
class Menu:

    def __init__(self):
        pass

    def options(self,):
        options = [
            {
                "id": 1,
                "opt": "Create default name empty folders ",
                "click": lambda _: print('option 2 test')
            },
            {
                "id": 2,
                "opt": "Create custom name empty folders ",
                "click": lambda _: print('option 2 test')
            },
            {
                "id": 3,
                "opt": "Create default name empty folders with note file",
                "click": lambda _: print('option 2 test')
            },
            {
                "id": 4,
                "opt": "Create custom name folders with note file ",
                "click": lambda _: print('option 2 test')
            },
            {
                "id": 5,
                "opt": "Close app ",
                "click": lambda _: print('option 2 test')
            },

        ]
        # print("\n###  M E N U  ###\n")
        # for option in options:
        #     print(f"{option['id']}: {option['opt']}")

        return options #int(input("Type option number and press enter:"))