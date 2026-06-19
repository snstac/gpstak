import xml.etree.ElementTree as ET

import gpstak.gpstak as gpstak


def test_cot_event_uses_standard_point_and_hostname_source():
    event = gpstak.cot_event(
        {"lat": 37.123456, "lon": -122.654321, "altHAE": 12.5, "epx": 3, "epy": 4},
        "GPSTAK-test-host",
        "a-f-G",
        10,
        "test-host",
    )

    cot = ET.fromstring(event)
    assert cot.get("uid") == "GPSTAK-test-host"
    point = cot.find("point")
    assert point is not None
    assert point.get("lat") == "37.1234"
    assert point.get("lon") == "-122.6543"
    assert point.get("hae") == "12.5"
    detail = cot.find("detail")
    assert detail is not None
    remarks = detail.find("remarks")
    assert remarks is not None
    assert remarks.text == "Network GPS from test-host"
