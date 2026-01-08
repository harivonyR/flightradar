# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:44:20 2026

@author: Lenovo
"""

from api import get_flights, get_flight_details


if __name__ == "__main__" :
    
    """
    Scrape Flights List Within a bounds
    
    """
    
    flights = get_flights(
        lat_max=16.148021798670523,
        lat_min=14.968157569699077,
        lon_min=107.106808551683,
        lon_max=108.29397601101239,
    )
    
    print(f"Flights found: {len(flights)}")
    
    
    """
    Trigger ClickHandler and scrape more flight details
    
    """
    flight = flights[0]
    flight_detail = get_flight_details(flight["id"])
    
    print(f"Flights found: {len(flights)}")