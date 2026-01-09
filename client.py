# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 19:39:54 2026

@author: Lenovo
"""

import requests
from typing import Dict, Any
from config import BASE_PARAMS, HEADERS
from bs4 import BeautifulSoup
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
        Take a raw response as input and return the JSON data
        
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

def fetch_airlines():
    
    airlines_url = "https://www.flightradar24.com/data/airlines"
    
    html_header = HEADERS.copy()
    html_header["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    
    response = requests.get(airlines_url, headers=html_header, timeout=30)
    html_content = response.text
    
    airlines_data = []
    
    # Parse HTML content.
    soup = BeautifulSoup(html_content, "html.parser")
    
    tbody = soup.find("tbody")

    if not tbody:
        return []
    
    # Extract data from HTML content.
    tr_elements = tbody.find_all("tr")
    
    for tr in tr_elements:
        td_notranslate = tr.find("td", class_="notranslate")
        
        if td_notranslate:
            a_element = td_notranslate.find("a", href=lambda href: href and href.startswith("/data/airlines"))
            
            if a_element:
                td_elements = tr.find_all("td")

                # Extract airline name.
                airline_name = a_element.get_text(strip=True)

                if len(airline_name) < 2:
                    continue

                # Extract IATA / ICAO codes.
                iata = None
                icao = None

                if len(td_elements) >= 4:
                    codes_text = td_elements[3].get_text(strip=True)

                    if " / " in codes_text:
                        parts = codes_text.split(" / ")

                        if len(parts) == 2:
                            iata = parts[0].strip()
                            icao = parts[1].strip()

                    elif len(codes_text) == 2:
                        iata = codes_text

                    elif len(codes_text) == 3:
                        icao = codes_text
                
                # Extract number of aircrafts.
                n_aircrafts = None

                if len(td_elements) >= 5:
                    aircrafts_text = td_elements[4].get_text(strip=True)

                    if aircrafts_text:
                        n_aircrafts = aircrafts_text.split(" ", maxsplit=1)[0].strip()
                        n_aircrafts = int(n_aircrafts)

                airline_data = {
                    "Name": airline_name,
                    "ICAO": icao,
                    "IATA": iata,
                    "n_aircrafts": n_aircrafts
                }
                
                airlines_data.append(airline_data)
    
    return airlines_data

if __name__ == "__main__" :
    airlines_url = "https://www.flightradar24.com/data/airlines"
    
    html_header = HEADERS.copy()
    html_header["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    response = requests.get(airlines_url, headers=html_header, timeout=30)
    html_content = response.text
    
    airlines_data = []
    
    # Parse HTML content.
    soup = BeautifulSoup(html_content, "html.parser")
    #airlines = fetch_airlines()
    
    tbody = soup.find("tbody")
    
    # Extract data from HTML content.
    tr_elements = [tr for tr in tbody.find_all("tr") if "header" not in (tr.get("class") or [])]
    
    tr_element = tr_elements[1]
