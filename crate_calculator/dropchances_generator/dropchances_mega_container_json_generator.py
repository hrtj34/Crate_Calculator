from pathlib import Path
import json

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

with open(Path("crate_calculator/dropchances/mega_container_dropchances.json"), "w") as file_path:
    json.dump(dropchances_mega_container, file_path)