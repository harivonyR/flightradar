# flightradar
Simple Scraper to learn fundamental.


## Get Started
### Setup Dependencies :
```bash
pip install requests beautifulsoup4 brotli
```

## Project Structure
```
.
├── main.py     # Entry point / usage examples
├── api.py      # Public API (endpoints)
├── client.py   # Network layer (HTTP, decoding)
├── mapping.py  # FlightRadar24 data mapping & parsing
└── README.md
```

## Endpoint
### 1. get_flight : 
Scrape flights within a geographic area (latitude & longitude)

```python

from api import get_flights

flights = get_flights(
    lat_max=16.148021798670523,
    lat_min=14.968157569699077,
    lon_min=107.106808551683,
    lon_max=108.29397601101239,
)

print(f"Flights found: {len(flights)}")

```

### 2. get_flight_details :
Retrieve flight details using a flight ID.

```python
from api import get_flight_details

flight_id = "3dd65321"
flight_detail = get_flight_details(flight_id)
```

### 3. get_airlines :
Retrieve the list of airlines.
```python
from api import get_airlines

airlines = get_airlines()
print(f"Airlines found: {len(airlines)}")

```