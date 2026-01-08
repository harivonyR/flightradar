# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:41:51 2026

@author: Lenovo
"""
from typing import List, Dict, Any

FEEDS_MAPPING = {
    "icao_24bit": 0,
    "latitude": 1,
    "longitude": 2,
    "heading": 3,
    "altitude": 4,
    "ground_speed": 5,
    "squawk": 6,
    "radar_id": 7,
    "aircraft_code": 8,
    "registration": 9,
    "time": 10,
    "origin_airport_iata": 11,
    "destination_airport_iata": 12,
    "number": 13,
    "on_ground": 14,
    "vertical_speed": 15,
    "callsign": 16,
    #"index17" : not set
    "airline_icao": 18,
}

def map_flight(feed: List[Any]) -> Dict[str, Any]:
    """
        Match result with Feed Mapping and return Key Value Result

    """
    flight = {}

    for field, idx in FEEDS_MAPPING.items():
        value = feed[idx] if idx < len(feed) else None
        flight[field] = value if value not in ("", None) else None

    # Derived fields
    number = flight.get("number")
    flight["airline_iata"] = number[:2] if number else None

    return flight