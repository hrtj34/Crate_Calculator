from pathlib import Path
import json

dropchances_mystery_boxes = {
    "mystery box iii": {
        "mystery certificate": {1: 0.15}, 
        "premium account": {7: 0.0684, 14: 0.0342, 30: 0.0158, 60: 0.0132, 90: 0.0105, 180: 0.0053, 360: 0.0026},
        "gold": {1000: 0.1484, 2000: 0.0928, 3500: 0.0371, 5000: 0.0124, 10000: 0.0063, 50000: 0.0028, 300000: 0.0002},
        "mystery profile background": {1: 0.01},
        "lightning catcher animated avatar": {1: 0.02},
        "mystery charm iii": {1: 1.0}
    },

    "mystery box ii": {
        "mystery certificate": {1: 0.1}, 
        "premium account": {1: 0.0957, 2: 0.0479, 3: 0.0319, 7: 0.0138, 14: 0.0069, 30: 0.0032, 270: 0.0005},
        "gold": {100: 0.1241, 200: 0.0775, 500: 0.031, 1500: 0.0104, 3000: 0.0053, 5000: 0.0016, 150000: 0.0002},
        "lightning catcher animated avatar": {1: 0.0036},
        "mystery charm iii": {1: 1.0}
    },

    "mystery box i": {
        "mystery certificate": {1: 0.05},
        "gold": {100: 0.1191, 200: 0.0744, 500: 0.0298, 1500: 0.01, 3000: 0.0051, 5000: 0.0015, 100000: 0.0001},
        "mystery charm ii": {1: 1.0},
        "gold booster": {1: 0.0976, 2: 0.0488, 3: 0.0325, 5: 0.0141, 10: 0.007}
    },

    "mystery charm ii": {
        "mystery box ii": {1: 1.0/15}
    },

    "mystery charm iii": {
        "mystery box iii": {1: 1.0/10}
    },

    "mystery certificate": {
        "gold": {1250: 5 * 0.0093, 1750: 6 * 0.0111, 2500: 21 * 0.0051, 3750: 39 * 0.0023, 5000: 8 * 0.0208, 7500: 18 * 0.0093}
    }
}

with open(Path("crate_calculator/dropchances/mystery_box_dropchances.json"), "w") as file_path:
    json.dump(dropchances_mystery_boxes, file_path)