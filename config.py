# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:41:06 2026

@author: Lenovo
"""

HEADERS = {
    "accept": "application/json",
    "accept-encoding": "gzip, br",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "origin": "https://www.flightradar24.com",
    "referer": "https://www.flightradar24.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 6.1) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.88 Safari/537.36"
    ),
}

BASE_PARAMS = {
    "faa": "1",
    "satellite": "1",
    "mlat": "1",
    "flarm": "1",
    "adsb": "1",
    "gnd": "1",
    "air": "1",
    "vehicles": "1",
    "estimated": "1",
    "maxage": "14400",
    "gliders": "1",
    "stats": "1",
    "limit": "5000",
}