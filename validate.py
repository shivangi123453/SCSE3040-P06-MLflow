"Is this order usable?"


def is_valid_order(order):
    "True if the order passes every rule."
    if(order["distance_km"] <= 0):
        return False
    if(order["prep_time_min"] < 0):
        return False
    if(order["traffic_level"] not in (1,2,3)):
        return False
    if(order["rain"] not in (0,1)):
        return False
    return True

if __name__ == "__main__":
    test_orders = [
        {"distance_km": 7.0, "prep_time_min": 25.0, "traffic_level": 3, "rain": 0},
        {"distance_km": 0, "prep_time_min": 25.0, "traffic_level": 3, "rain": 0},
        {"distance_km": 5.0, "prep_time_min": -1, "traffic_level": 2, "rain": 1},
        {"distance_km": 5.0, "prep_time_min": 10.0, "traffic_level": 5, "rain": 0},
        {"distance_km": 5.0, "prep_time_min": 10.0, "traffic_level": 2, "rain": 2},
    ]

    passed = 0

    for i, order in enumerate(test_orders, start=1):
        result = is_valid_order(order)
        expected = i == 1
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | Valid order: {result}")

        if status == "PASS":
            passed += 1

    print(f"\nValidation tests passed: {passed}/{len(test_orders)}")

