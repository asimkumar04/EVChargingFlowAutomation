import time
import math


# Distance calculation

def calculate_distance_km(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius (KM)

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(d_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def test_poi(poi_api):

    base_lat = 51.5074
    base_lon = 0.1278

    params = {
        "latitude": "51.5074",
        "longitude": "0.1278",
        "maxresults": 5,
        "distance": 10
    }


    # Start timer
    start_time = time.time()

    response = poi_api.get_poi(params=params)

    response_time_ms = (time.time() - start_time) * 1000



    # Validate response time is less than 1000 ms
    assert response_time_ms < 1000, f"Response too slow: {response_time_ms:.2f} ms"


    # Validate status code is 200
    assert response.status_code == 200


    # Validate Response type
    data = response.json()
    assert isinstance(data, list), "Response should be a list of POIs"


    # Validate Exact results count
    assert len(data) == 5, f"Expected 5 POIs, got {len(data)}"


    # 5. Validate POI loop
    for poi in data:

        # ID check
        assert "ID" in poi, "Missing POI ID"

        # AddressInfo check
        assert "AddressInfo" in poi, f"Missing AddressInfo for POI {poi.get('ID')}"

        address = poi["AddressInfo"]

        # Lat/Lon checks
        assert "Latitude" in address
        assert "Longitude" in address

        lat = address["Latitude"]
        lon = address["Longitude"]

        assert isinstance(lat, (float, int))
        assert isinstance(lon, (float, int))


        # Validate Number of points (Connections)
        if "Connections" in poi:
            assert isinstance(poi["Connections"], list)
            assert len(poi["Connections"]) >= 0


    # Validate Distance of POI is in 10 KM radius
        distance_km = calculate_distance_km(base_lat, base_lon, lat, lon)

        assert distance_km <= 10, (
         f"POI {poi.get('ID')} outside 10km radius: {distance_km:.2f} km"
        )