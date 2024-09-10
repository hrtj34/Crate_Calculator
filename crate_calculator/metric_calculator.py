from typing import Callable
from dropchance_reader import DropchanceReader

class MetricCalculator:
    def __init__(self, metric: Callable[[int, int, int], int] = lambda x, y, z : x * y * z, metric_dictionary: dict = {}) -> None:
        self.metric = metric
        self.metric_dictionary = metric_dictionary

    def calculate_item_metric(self, item: str, dropchances_boxes: DropchanceReader, item_target: str = None, items_being_calculated: dict = {}) -> tuple[float, dict]:
        if item in self.metric_dictionary and self.metric_dictionary[item]:
            return self.metric_dictionary[item], {item: self.metric_dictionary[item]}
        
        if not item in items_being_calculated:
            items_being_calculated[item] = 0
        else:
            items_being_calculated[item] += 1
            if items_being_calculated[item] > 10: return 0, {item: 0}

        aggregated_metric = 0
        metric_by_item = {}
        
        for drop_item, dropchances in dropchances_boxes.read_dropchance(item).items():
            drop_item_metric, _ = self.calculate_item_metric(drop_item, dropchances_boxes, item_target=item_target, items_being_calculated=items_being_calculated)

            for drop_amount, dropchance in dropchances.items():
                drop_metric = self.metric(drop_item_metric, int(drop_amount), dropchance)
                if item_target and drop_item == item_target:
                    drop_metric = dropchance                    # Could be something like target_metric

                aggregated_metric += drop_metric
                metric_by_item[drop_item] = metric_by_item.get(drop_item, 0) + drop_metric

        if aggregated_metric:
            self.metric_dictionary[item] = aggregated_metric
        return aggregated_metric, metric_by_item