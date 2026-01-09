# -*- coding: utf-8 -*-
"""
API layer – FlightRadar endpoints
"""

from typing import Dict, Any, List

from client import fetch_feed, fetch_flight_details, fetch_airlines
from mapping import map_flight


def get_flights(
    lat_max: float,
    lat_min: float,
    lon_min: float,
    lon_max: float
) -> List[Dict[str, Any]]:
    """
    Return list of flights inside bounds (latitude & longitude)
    """

    bounds = f"{lat_max},{lat_min},{lon_min},{lon_max}"

    try:
        raw_feed = fetch_feed(bounds)
    except Exception as exc:
        return {
            "error": True,
            "endpoint": "get_flights",
            "message": "Unable to fetch live feed",
            "details": str(exc),
        }

    flights: List[Dict[str, Any]] = []

    for flight_id, feed in raw_feed.items():
        if not flight_id or not flight_id[0].isdigit():
            continue

        try:
            flight = map_flight(feed)
            flight["id"] = flight_id
            flights.append(flight)
        except Exception:
            # Skip corrupted flight entry (defensive scraping)
            continue

    return flights


def get_flight_details(flight_id: str) -> Dict[str, Any]:
    """
    Take a flight_id, call click handler and return flight details
    """

    try:
        return fetch_flight_details(flight_id)
    except Exception as exc:
        return {
            "error": True,
            "endpoint": "get_flight_details",
            "flight_id": flight_id,
            "message": "Unable to fetch flight details",
            "details": str(exc),
        }


def get_airlines() -> Dict[str, Any]:
    """
    Return airlines list
    """

    try:
        return fetch_airlines()
    except Exception as exc:
        return {
            "error": True,
            "endpoint": "get_airlines",
            "message": "Unable to fetch airlines list",
            "details": str(exc),
        }
