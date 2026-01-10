# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:44:20 2026

@author: harivonyratefiarison
"""

from api import get_flights, get_flight_details, get_airlines


if __name__ == "__main__" :
    
    """    1. Scrape Flights List Within a bounds    """
    
    flights = get_flights(
        lat_max = 16.148021798670523,
        lat_min = 14.968157569699077,
        lon_min = 107.106808551683,
        lon_max = 108.29397601101239,
    )
    
    print(f"Flights found: {len(flights)}")
    
    
    """    2. Track Flight Details From an ID   """
    
    flightID = "3dd65321"    # A333-KE-KAL Registration : HL8025
    flight_detail = get_flight_details(flightID)
    #print(f"Flights found: {flight_detail}")
    
    
    """    3. Get List Of All Airlines Available   """
    
    airlines = get_airlines()
    print(f"Airlines found: {len(airlines)}")
    
    
    
    
    
    
    
    