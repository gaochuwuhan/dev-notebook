import arrow

a1=(arrow.now().datetime)
timestamp = round(a1.timestamp() * 1000)
print(round(arrow.get("1900-01-01").float_timestamp * 1000))