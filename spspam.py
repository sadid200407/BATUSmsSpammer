# -*- coding: utf-8 -*-
import os

from send_requests import send_requests
from check_input import CheckInput
from colors import BOLD, FG, RESET_ALL
from text import banner, cursor, replace


def clear_screen():
    return (
        os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    )

def main():
    clear_screen()
    print(banner, replace + "Enter your phone number:" + RESET_ALL, sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(replace + "Enter the number of cycles:" + RESET_ALL)
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    if count >= 10:
        print(
            f"{FG.green}* You entered more than 10 cycles, "
            f"after the 5th the spam rate will decrease{RESET_ALL}"
        )
    send_requests(phone, count)
    clear_screen()
    print(
        BOLD + f"{FG.green}Done!",
        f"Telephone: {FG.purple}{phone}",
        f"{FG.green}Number of cycles: {FG.purple}{count}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
