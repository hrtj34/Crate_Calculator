from pathlib import Path
import json

dropchances_massive_container = {
    "massive container": {
        "massive container tank": {1: 1.0}, 
        "massive container group container": {1: 1.0},
        "massive charm": {1: 1.0},
        "massive container group quest": {1: 1.0}
    },

    "massive container tank": {
        "gold": {3750: 24 * 0.027, 5000: 6 * 0.027, 7500: 7 * 0.027}
    },

    "massive container group container": {
        "mega container": {2: 0.0602, 3: 0.0422, 5: 0.0301},
        "black box i": {2: 0.1205, 3: 0.0783, 5: 0.0602},
        "mystery box i": {3: 0.1205, 5: 0.0904, 10: 0.0422},
        "collect em all container": {3: 0.1205, 5: 0.0904, 7: 0.0482},
        "awesome container": {1: 0.0482, 2: 0.0301, 3: 0.0181}
    },

    "massive charm": {
        "massive container": {1: 1.0/15}
    },

    "massive container group quest": {
        "mega container": {1: 0.0829, 3: 0.0829, 5: 0.0829},
        "mystery box i": {3: 0.0829, 5: 0.0829, 10: 0.0829},
        "collect em all container": {1: 0.0829, 3: 0.0829, 5: 0.0829},
        "awesome container": {1: 0.0829, 2: 0.0829, 3: 0.0829},
        "massive background": {1: 0.0049}
    }
}

with open(Path("crate_calculator/dropchances/massive_container_dropchances.json"), "w") as file_path:
    json.dump(dropchances_massive_container, file_path)