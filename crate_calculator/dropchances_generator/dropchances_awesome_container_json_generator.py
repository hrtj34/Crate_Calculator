from pathlib import Path
import json

dropchances_awesome_container = {
    "awesome container": {
        "awesome container tank": {1: 0.1}, 
        "awesome container group container": {1: 0.5},
        "premium account": {7: 0.2083, 14: 0.0312, 30: 0.0104},
        "gold": {100: 0.1187, 200: 0.095, 500: 0.0831, 750: 0.0712, 1000: 0.0594, 1500: 0.0309, 3000: 0.019, 5000: 0.0142, 10000: 0.0083, 100000: 0.0002},
        "lockbox key": {1: 0.07},
        "awesome charm": {1: 1.0},
    },

    "awesome container tank": {
        "gold": {2500: 2.5 * 10 * 0.0028, 3750: 13 * 10 * 0.0028, 5000: 4 * 10 * 0.0028, 7500: 10 * 10 * 0.0028}
    },

    "awesome container group container": {
        "collect em all container": {1: 2 * 0.1667},
        "mystery box i": {1: 2 * 0.1667},
        "black box i": {1: 2 * 0.1667}
    },

    "awesome charm": {
        "awesome container": {1: 0.1}
    }
}

with open(Path("crate_calculator/dropchances/awesome_container_dropchances.json"), "w") as file_path:
    json.dump(dropchances_awesome_container, file_path)