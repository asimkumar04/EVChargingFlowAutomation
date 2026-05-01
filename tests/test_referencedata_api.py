import time


def test_referencedata_api(reference_api):

    start_time = time.time()

    # Call reference API
    response = reference_api.get_reference_data()

    response_time_ms = (time.time() - start_time) * 1000

    # Validate response time is less than 1000 ms
    assert response_time_ms < 1000, f"Too slow: {response_time_ms:.2f} ms"

    # Validate status code is 200
    assert response.status_code == 200

    # Parse response
    data = response.json()

    # Validate response structure
    assert isinstance(data, dict)


    # Validate response has chargerTypes, statusTypes and connectionTypes sections
    expected_sections = ["ChargerTypes", "StatusTypes", "ConnectionTypes"]

    for section in expected_sections:

        # Check if all the mentioned section exists
        assert section in data, f"Missing section: {section}"

        items = data.get(section)

        # Handle None safely
        if items is None:
            print(f"Skipping {section} as it is None")
            continue

        # Validate each type is a list
        assert isinstance(items, list), f"{section} should be a list"

        # Validate each item has ID and title
        for item in items:
            assert "ID" in item, f"Missing ID in {section}"
            assert "Title" in item, f"Missing Title in {section}"

    # ChargerTypes validation to verify fast and slow chargers
    charger_types = data.get("ChargerTypes")

    assert charger_types is not None, "ChargerTypes is missing"
    assert isinstance(charger_types, list), "ChargerTypes should be a list"

    for charger_type in charger_types:
        charger_isfastchargecapable = charger_type.get("IsFastChargeCapable")

        assert isinstance(
            charger_isfastchargecapable, bool
        ), f"IsFastChargeCapable should be boolean, got {type(charger_isfastchargecapable)}"

    # Validate StatusTypes has unique IDs
    status_types = data.get("StatusTypes")

    assert status_types is not None, "StatusTypes is missing"
    assert isinstance(status_types, list), "StatusTypes should be a list"

    status_ids = [s.get("ID") for s in status_types]

    # Ensure no None IDs
    assert None not in status_ids, "Some StatusTypes have missing ID"

    # Check uniqueness
    assert len(status_ids) == len(set(status_ids)), "Duplicate IDs found in StatusTypes"