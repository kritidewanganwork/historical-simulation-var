def basel_traffic_lights(breach_count: int, confidence_level: float) -> dict:
    """
    Basel Traffic Light classification for VaR backtesting.
    """
    if confidence_level == 0.99:
        if breach_count <= 4:
            zone = "Green"
            multiplier = 3
        elif 5 <= breach_count <= 9:
            zone = "Yellow"
            multiplier = 3.5
        else:
            zone = "Red"
            multiplier = 4
    
    else:
        raise ValueError("Basel traffic light implemented for 99% VaR only.")
    
    return {
        "Zone": zone,
        "Capital Multiplier": multiplier,
        "Breaches": breach_count
    }
