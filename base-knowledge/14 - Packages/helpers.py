from colorama import Fore, init


def display(val):
    init(autoreset=True)
    print(Fore.RED + val)
