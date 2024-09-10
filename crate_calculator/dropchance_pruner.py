'''
Pseudo-Median for limited number of draws

Takes:
- number of draws
- item
- dropchances

Yields:
- 'Expected Median values'

For Expected Median Values, an item is only considered if it is expected to drop 
in exactly or more than half of all draw-series of length equal to the number of draws, 
if repeated sufficiently often enough

Algorithmic steps:
1. Item probabilities are aggregated for a single draw
2. Probability to receive item at least once in (number of draws) is calculated
3. Items with a probability lower than 50% over the draw-series are excluded
4. Expected Value is calculated with the rest

Items might need to be grouped to avoid that items with low drop chances 
which are grouped together in crates (with one in the group being guaranteed to drop)
are completely disregarded. So the draw-series probabilities check only checks 
if the group passes, not if the individual items pass

After an item gets removed the percentages of the remaining items in the group 
must be increased, so the group has the same probability as a whole again.
The dropchance structure needs to consider the groups by either generating 'subcrates' 
(e.g. "mystery box i group i") or (if only one item type is in the group) 
by having all item drop probabilities of the group in the same dropchance object 
of an item (as it is already, e.g. "gold" in several crates) 
WORK IN PROGRESS
'''


class DropchancePruner:
    def __init__(self) -> None:
        pass

    def decision_metric(self, dropchances_item: dict) -> list:
        pass



    def get_group_probability(self, dropchances: dict|float) -> float:
        if not isinstance(dropchances, dict):
            return dropchances
        
        probability = 0
        for dropchance in dropchances.values():
            probability += self.get_group_probability(dropchance)
        
        return probability

    def divide_evenly_per_group(self, num_to_divide: float, dropchances: dict) -> None:
        num_items = len(dropchances)
        num_divided = num_to_divide / num_items
        for item, dropchance in dropchances.items():
            if not isinstance(dropchance, dict):
                dropchances[item] += num_divided
            else:
                self.divide_evenly_per_group(num_divided, dropchance)

    # Expects dropchances for a container-like item
    def dropchance_pruning(self, dropchances: dict|float, num_draws: int):
        if not isinstance(dropchances, dict):
            return
        
        group_probability = self.get_group_probability(dropchances)

        num_items_in_group = len(dropchances)
        probability_to_reach = group_probability / num_items_in_group

        group_excess_dropchance = 0
        dropped_items = []

        for item, dropchance in dropchances.items():
            item_probability = self.get_group_probability(dropchance)
            item_probability_at_least_once = 1 - (1 - item_probability)**num_draws

            if item_probability_at_least_once < probability_to_reach:
                group_excess_dropchance += item_probability
                dropped_items.append(item)
            else:
                self.dropchance_pruning(dropchance, num_draws)
        
        for item in dropped_items:
            dropchances.pop(item, None)
        
        self.divide_evenly_per_group(group_excess_dropchance, dropchances)
