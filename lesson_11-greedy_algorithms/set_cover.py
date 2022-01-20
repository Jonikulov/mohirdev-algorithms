# Greedy Set Cover
from random import sample
from pprint import pprint
import pickle

zones = set(range(1,31))

buildings = {
    'B01':set(sample(zones,3)), 
    'B02':set(sample(zones,4)),
    'B03':set(sample(zones,4)),
    'B04':set(sample(zones,5)),
    'B05':set(sample(zones,5)),
    'B06':set(sample(zones,3)),
    'B07':set(sample(zones,2)),
    'B08':set(sample(zones,5)),
    'B09':set(sample(zones,4)),
    'B10':set(sample(zones,3)),
    'B11':set(sample(zones,5)),
    'B12':set(sample(zones,2)),
    'B13':set(sample(zones,3)),
    'B14':set(sample(zones,5))
    }

part_zone = []
for building in buildings.values():
    for i in building:
        part_zone.append(i)
part_zone = set(part_zone)

## writing 15 buildings dictionary as pickle
# buildings['B15'] = zones - part_zone
# with open('buildings.pickle', 'wb') as file:
#     pickle.dump(buildings,file)

# reading pickle file
with open('buildings.pickle', 'rb') as file:
    buildings = pickle.load(file)


def greedy_set_cover(zones, buildings):
    best_cover = set()

    while zones:
        biggest_cover = {}
        for building in buildings.keys():
            # checking if bigger and if searched
            if len(buildings[building])>len(biggest_cover) and building not in best_cover:
                biggest_cover = building
        # adding coverd building
        best_cover.add(biggest_cover)
        # subtracting elements that are in zones
        zones = zones - buildings[biggest_cover]

    return best_cover


result = greedy_set_cover(zones, buildings)
pprint(buildings)
print('Covered sets:', result)