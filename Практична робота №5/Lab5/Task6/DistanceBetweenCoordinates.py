import math
from itertools import combinations

def haversine(coord1, coord2, radius=6371):
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

def find_closest_pair(coords):
    pairs = list(combinations(coords, 2))
    distances = map(lambda pair: (pair, haversine(*pair)), pairs)
    closest_pair = min(distances, key=lambda x: x[1])
    return closest_pair

coordinates = [
    (48.8566, 2.3522),
    (51.5074, -0.1278),
    (40.7128, -74.0060),
    (34.0522, -118.2437),
    (35.6895, 139.6917),
    (55.7558, 37.6173),
    (52.52, 13.405),
    (41.9028, 12.4964),
    (45.4642, 9.19),
    (50.1109, 8.6821)
]

pair, distance = find_closest_pair(coordinates)
print(f"The closest couple: {pair[0]} and {pair[1]}")
print(f"The distance between them: {distance:.2f} km")
