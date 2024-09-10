from pathlib import Path
import json

dropchances_collect_em_all_container = {
    "collect em all container": {
        "collect em all container tank": {1: 0.05},
        "gold charm 7": {1: 0.95}
    },

    "collect em all container tank": {
        "gold": {1250: 3 * 20 * 0.0003, 1750: 6 * 20 * 0.0003, 2500: 17 * 20 * 0.0003, 3750: 38 * 20 * 0.0003, 5000: 6 * 20 * 0.0003, 7500: 15 * 20 * 0.0003}
    }
}

with open(Path("crate_calculator/dropchances/collect_em_all_container_dropchances.json"), "w") as file_path:
    json.dump(dropchances_collect_em_all_container, file_path)