# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:39:54 2026

@author: Lenovo
"""

import requests
from typing import Dict, Any
from config import BASE_PARAMS, HEADERS
import gzip
import brotli
import json

_DECODERS = {
    "": lambda x: x,
    "gzip": gzip.decompress,
    "br": brotli.decompress,
}


def decode_response(response: requests.Response) -> Dict[str, Any]:
    """
        Take a raw response in input and return the JSON data
        
    """
    response.raise_for_status()

    content = response.content
    encoding = response.headers.get("Content-Encoding", "")
    content_type = response.headers.get("Content-Type", "")

    decoder = _DECODERS.get(encoding)
    if decoder:
        try:
            content = decoder(content)
        except Exception:
            pass

    if "application/json" not in content_type:
        raise ValueError("Response is not JSON")

    return json.loads(content)

def fetch_feed(bounds: str) -> Dict[str, Any]:
    """
        Return decoded data from flightradar live-feed
        
    """
    base_url = "https://data-cloud.flightradar24.com/zones/fcgi/feed.js"

    params = BASE_PARAMS.copy()
    params["bounds"] = bounds

    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{base_url}?{query}"

    response = requests.get(url, headers=HEADERS, timeout=30)
    return decode_response(response)

def fetch_flight_details(flightID: str ) -> Dict[Any, Any]:
    """
        Trigger clickhandler and return Flight details
    
    """

    flight_data_url = "https://data-live.flightradar24.com/clickhandler/?flight={}"
    
    response = requests.get(flight_data_url.format(flightID), headers=HEADERS, timeout=30)
    
    return decode_response(response)