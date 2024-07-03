def convert_to_eth(amount: float, rate: float) -> float:
    return amount / rate

def convert_from_eth(amount: float, rate: float) -> float:
    return amount * rate