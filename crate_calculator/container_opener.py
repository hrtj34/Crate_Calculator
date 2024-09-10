'''
Simply gives example drops based on dropchances. No harm, no gain :)

Problematic: Certain items drop in groups, that is there is a certain possibility 
that one item out of the group drops. for the purpose of pruning, these groups have been formalised. 
However, for that reason it is impossible to guarantee that no more than one item of the group drops. 
As Crates have multiple drops. it is also difficult to draw the limits (where 100% is full, hence the groups).
That is, it is difficult to determine which items constitute part of a group 
and furthermore if an item is a group or an actual dropable item
'''
from random import uniform
from math import ceil
from dropchance_pruner import DropchancePruner
from dropchance_reader import DropchanceReader

class ContainerOpener:
    def __init__(self) -> None:
        pass

    def select_item_in_group(self, group_dropchances: dict, drops: dict) -> None:
        dropchance_pruner = DropchancePruner()

        upper_bound_probability = ceil(dropchance_pruner.get_group_probability(group_dropchances))
        random_number = uniform(0.0, upper_bound_probability)
        covered_chance_space = 0.0

        for item, item_dropchances in group_dropchances.items():
            for amount, dropchance in item_dropchances.items():
                covered_chance_space += dropchance
                if covered_chance_space > random_number:
                    drops[item] = drops.get(item, 0) + amount
                    return

    def open_container(self, container: str, num_opening: int, dropchances: DropchanceReader) -> dict:
        dropchance_pruner = DropchancePruner()
        drops = {}
        
        for i in range(num_opening):
            groups_list = []
            all_dropchances = dropchances.read_dropchance(container, groups_list)
            for group in groups_list:
                group_dropchances = {}
                for item in group:
                    group_dropchances[item] = all_dropchances[item]
                self.select_item_in_group(group_dropchances, drops)

            


        cascaded_drops = []
        secondary_drops = {}
        for drop, amount in drops.items():
            secondary_drop_candidate = self.open_container(drop, amount, dropchances)
            if secondary_drop_candidate:
                cascaded_drops.append(drop)
                secondary_drops |= secondary_drop_candidate

        for cascaded_drop in cascaded_drops:
            drops.pop(cascaded_drop, None)
            
        for item, amount in secondary_drops.items():
            drops[item] = drops.get(item, 0) + amount

        return drops


dropchances_mega_container = {
    "mega container": {
        "mega container tank": {1: 0.05}, 
        "mega container group container": {1: 0.2},
        "gold": {250: 0.3968, 300: 0.2645, 350: 0.1984, 500: 0.0827, 750: 0.0231, 1000: 0.0165, 1500: 0.0116, 3000: 0.0033, 5000: 0.0017, 10000: 0.001, 20000: 0.0002, 50000: 0.0001, 100000: 0.0001},
        "lockbox key": {1: 0.05},
        "gold charm 10": {1: 1.0},
        "gold booster": {5: 0.0588}
    },

    "mega container tank": {
        "gold": {1250: 4 * 20 * 0.0003, 1750: 7 * 20 * 0.0003, 2500: 17 * 20 * 0.0003, 3750: 37 * 20 * 0.0003, 5000: 8 * 20 * 0.0003, 7500: 17 * 20 * 0.0003}
    },

    "mega container group container": {
        "collect em all container": {1: 5 * 0.0635},
        "mystery box i": {1: 5 * 0.0635},
        "black box i": {1: 5 * 0.0635},
        "grand surprise container": {1: 5 * 0.0095}
    },
}
dropchance_reader = DropchanceReader(dropchances_mega_container)

container_opener = ContainerOpener()
drops = container_opener.open_container("mega container", 1, dropchance_reader)

print("Hi! :)")