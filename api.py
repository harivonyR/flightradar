# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:42:35 2026

@author: Lenovo
"""
from client import fetch_feed, fetch_flight_details
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


def get_flight_details(flightID: str ) -> Dict[Any, Any]:
    """
        Take a flightid, call a click handler and return flight details
    
    """
    
    flight_details = fetch_flight_details(flightID)
    """
    aircraft = self.__get_info(details.get("aircraft"), dict())
    airline = self.__get_info(details.get("airline"), dict())
    airport = self.__get_info(details.get("airport"), dict())
    history = self.__get_info(details.get("flightHistory"), dict())
    status = self.__get_info(details.get("status"), dict())
    
    trail = details.get("trail", list())
    time_details =  details.get("time", {})
    
    flight_details = {
        "aircraft" : aircraft,
        "airline" : airline,
        "airport" : airport,
        
        "history" : history,
        "status" : status,
        
        "trail" : trail,
        "time_details" :  time_details
        }
    """
    
    return flight_details