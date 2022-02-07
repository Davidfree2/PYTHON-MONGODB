from colorama import Fore,Back,Style
from colorama import init


class Banner:
    def __init__(self):
        pass

    def banner(self):
        init()
        print(Fore.MAGENTA+ '''

    ████████╗ ██████╗ ██████╗  ██████╗ ██╗     ██╗███████╗████████╗
    ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗██║     ██║██╔════╝╚══██╔══╝
       ██║   ██║   ██║██║  ██║██║   ██║██║     ██║███████╗   ██║   
       ██║   ██║   ██║██║  ██║██║   ██║██║     ██║╚════██║   ██║   
       ██║   ╚██████╔╝██████╔╝╚██████╔╝███████╗██║███████║   ██║   
       ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                (control C to exit)
        ''')
        print(Style.RESET_ALL)


