# -*- coding: utf-8 -*-
import re
from .colors import RESET_ALL, BOLD, FG


class CheckInput:
    def verification_phone(self, phone: str) -> str:
        self.phone = phone
        try:
            phone = re.sub("[^0-9]", "", phone)  # оставляет только цифры
            if phone.startswith("0"):
                phone = "38" + phone
                return phone
            elif phone == "" or phone == " ":
                print(f"{BOLD + FG.red}Номер введён некорректно!{RESET_ALL}")
                exit()
            elif phone.startswith("+"):
                return phone[1:]
            else:
                return phone
        except Exception:
            print(f"{BOLD + FG.red}Номер введён некорректно!{RESET_ALL}")
            exit()

    def verification_cycles(self, cycles: str) -> int:
        try:
            self.cycles = cycles
            cycles = re.sub("[^0-9]", "", cycles)
            return int(cycles)
        except ValueError:
            print("\033[1;31m" + "Неправильное кол-во циклов!")
            exit()


if __name__ == "__main__":
    phone = input("Введите номер телефона: ")
    cycles = input("Введите колличество циклов: ")
    print(CheckInput().verification_phone(phone))
    print(CheckInput().verification_cycles(cycles))
