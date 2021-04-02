# -*- coding: utf-8 -*-
from user_agent import generate_user_agent

head = {
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

uklon1 = {
    "client_id": "6289de851fc726f887af8d5d7a56c635",
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

uklon2 = {
    "client_id": "6289de851fc726f887af8d5d7a56c635",
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

frisor = {
    "Content-type": "application/json",
    "Accept": "application/json, text/plain",
    "authorization": "Bearer yusw3yeu6hrr4r9j3gw6",
    "User-Agent": generate_user_agent(),
}

zakaz = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Referer": "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
    "User-Agent": generate_user_agent(),
    "x-chain": "megamarket",
}
