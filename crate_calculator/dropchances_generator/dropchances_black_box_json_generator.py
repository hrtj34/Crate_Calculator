from pathlib import Path
import json

dropchances_black_boxes = {
    "black box x": {
        "gold": {250000: 1},
        "shining crown animated avatar": {1 : 1},
        "riches vault profile background": {1: 1},
        "black certificate": {1: 1} 
    },

    "black box ix": {
        "black box x": {1: 1.0/4},
        "gold": {key: 1.0/8 for key in range(3000, 11000, 1000)},
        "gold booster": {key: 1.0/21 for key in range(10, 31, 1)},
        "black charm": {1: 1},
        "shining crown animated avatar": {1 : 3.0/20},
        "riches vault profile background": {1: 1.0/20}
    },

    "black box viii": {
        "black box x": {1: 1.0/20}, 
        "black box ix": {1: 1.0/5},
        "gold": {key: 1.0/7 for key in range(2000, 5500, 500)},
        "gold booster": {key: 1.0/13 for key in range(8, 21, 1)},
        "black charm": {1: 1},
        "shining crown animated avatar": {1 : 1.0/20},
        "riches vault profile background": {1: 1.0/50}
    },

    "black box vii": {
        "black box ix": {1: 1.0/20}, 
        "black box viii": {1: 1.0/5},
        "gold": {key: 1.0/5 for key in range(1500, 4000, 500)},
        "gold booster": {key: 1.0/8 for key in range(7, 15, 1)},
        "black charm": {1: 1},
        "shining crown animated avatar": {1 : 3.0/100},
        "riches vault profile background": {1: 1.0/100} 
    },

    "black box vi": {
        "black box viii": {1: 1.0/20}, 
        "black box vii": {1: 1.0/5},
        "gold": {key: 1.0/14 for key in range(1200, 2600, 100)},
        "gold booster": {key: 1.0/7 for key in range(6, 13, 1)},
        "black charm": {1: 1},
        "shining crown animated avatar": {1 : 1.0/50}
    },

    "black box v": {
        "black box vii": {1: 1.0/20}, 
        "black box vi": {1: 1.0/5},
        "gold": {key: 1.0/11 for key in range(1000, 2100, 100)},
        "gold booster": {key: 1.0/6 for key in range(5, 11, 1)},
        "black charm": {1: 1},
        "shining crown animated avatar": {1 : 1.0/100}
    },

    "black box iv": {
        "black box vi": {1: 1.0/20}, 
        "black box v": {1: 1.0/5},
        "gold": {key: 1.0/11 for key in range(500, 1600, 100)},
        "gold booster": {key: 1.0/5 for key in range(4, 9, 1)},
        "black charm": {1: 1}
    },

    "black box iii": {
        "black box v": {1: 1.0/20}, 
        "black box iv": {1: 1.0/5},
        "gold": {key: 1.0/7 for key in range(300, 1000, 100)},
        "gold booster": {key: 1.0/3 for key in range(3, 6, 1)},
        "black charm": {1: 1}
    },

    "black box ii": {
        "black box iv": {1: 1.0/20}, 
        "black box iii": {1: 1.0/5},
        "gold": {key: 1.0/5 for key in range(200, 700, 100)},
        "gold booster": {key: 1.0/3 for key in range(2, 5, 1)}
    },

    "black box i": {
        "black box iii": {1: 1.0/20}, 
        "black box ii": {1: 1.0/5},
        "gold": {key: 1.0/4 for key in range(100, 500, 100)},
        "gold booster": {key: 1.0/3 for key in range(1, 4, 1)}
    },

    "black charm": {
        "black certificate": {1: 1.0/33}
    },

    "black certificate": {
        "gold": {5000: 4 * 0.1, 7500: 3 * 0.1}
    }
}

with open(Path("crate_calculator/dropchances/black_box_dropchances.json"), "w") as file_path:
    json.dump(dropchances_black_boxes, file_path)