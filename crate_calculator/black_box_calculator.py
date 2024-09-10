from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

from dropchance_getter import DropchanceGetter
from metric_calculator import MetricCalculator
from dropchance_pruner import DropchancePruner
from dropchance_reader import DropchanceReader
'''
Structure Dictionary:
lootbox_dropchances_bbX = {
    "gold": {250000: 1},
    "shining crown animated avatar": {1 : 1},
    "riches vault profile background": {1: 1},
    "black certificate": {1: 1} 
}
'''

# black charm value is one 33th of black certificate value (33 black charms to get one cert)
# black certificate value is expected gold compensation
value_dictionary = {
    "gold": 1,
    "gold booster": 15,
    "premium account": 250,
    "lockbox key": 300,
    "gold charm 7": 1000 / 7,
    "gold charm 10": 100,
    "shining crown animated avatar": 10000,
    "riches vault profile background": 50000,
    "mystery profile background": 50000,
    "lightning catcher animated avatar": 10000,
    "massive background": 50000
}



dropchance_getter = DropchanceGetter()
data_with_dependencies = dropchance_getter.load_item_dropchances_with_dependencies("massive container")

dropchance_reader = DropchanceReader(data_with_dependencies)
dropchances_with_dependencies = dropchance_reader.read_all_dropchances()

dropchance_pruner = DropchancePruner()
for container_like in dropchances_with_dependencies.values():
    dropchance_pruner.dropchance_pruning(container_like, 5)

value_calculator = MetricCalculator(metric_dictionary=value_dictionary)
chance_calculator = MetricCalculator()

expected_value_item_1, expected_value_by_item_item_1 = value_calculator.calculate_item_metric("mystery box i", dropchance_reader)
expected_value_item_2, expected_value_by_item_item_2 = value_calculator.calculate_item_metric("mega container", dropchance_reader)
expected_value_item_3, expected_value_by_item_item_3 = value_calculator.calculate_item_metric("massive container", dropchance_reader)
print("Hi! :)")

box_types = (
    "Mystery Box I",
    "Mega Container",
    "Massive Container"
)

weight_counts = {}
for key in (expected_value_by_item_item_1 | expected_value_by_item_item_2 | expected_value_by_item_item_3).keys():
    weight_counts[key] = np.array([expected_value_by_item_item_1.get(key, 0), expected_value_by_item_item_2.get(key, 0), expected_value_by_item_item_3.get(key, 0)])

width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(box_types, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Expected gold gain from box by item")
ax.legend(loc="upper right")

plt.show()