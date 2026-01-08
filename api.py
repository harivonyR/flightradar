# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:42:35 2026

@author: Lenovo
"""
from client import fetch_feed
from typing import Dict, Any,List
from mapping import map_flight

def get_flights(lat_max: float, lat_min: float, lon_min: float, lon_max: float) -> List[Dict[str, Any]]:
    """
        Return List of Flight found inside bounds (latitude & longitude)
    
    """
    
    bounds = f"{lat_max},{lat_min},{lon_min},{lon_max}"

    raw_feed = fetch_feed(bounds)

    flights = []

    for flight_id, feed in raw_feed.items():
        if not flight_id or not flight_id[0].isdigit():
            continue

        flight = map_flight(feed)
        flight["id"] = flight_id
        flights.append(flight)

    return flights