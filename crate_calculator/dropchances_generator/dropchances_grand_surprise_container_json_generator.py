from pathlib import Path
import json

dropchances_grand_surprise_container = {
    "grand surprise container": {
        "m60 container": {1: 0.025},
        "k-91 container": {1: 0.025},
        "pudel container": {1: 0.025},
        "skoda t 45 container": {1: 0.025},
        "amx 13 57 container": {1: 0.025},
        "astron rex container": {1: 0.025},
        "object 260 container": {1: 0.025},
        "b-c bourrasque container": {1: 0.025},
        "altproto amx 30 container": {1: 0.025},
        "tl-7-120 container": {1: 0.025},
        "type 64 container": {1: 0.025},
        "concept 1b container": {1: 0.025},
        "bofors tornvagn container": {1: 0.025},
        "wz-111 5a container": {1: 0.025},
        "smasher container": {1: 0.025},
        "t54e2 container": {1: 0.025},
        "titan h-nd container": {1: 0.025},
        "emil 1951 container": {1: 0.025},
        "leo container": {1: 0.025},
        "object 268 version 4 container": {1: 0.025},
        "bretagne panther container": {1: 0.025},
        "skoda t 27 container": {1: 0.025},
        "pz iv s container": {1: 0.025},
        "strv k container": {1: 0.025},
        "skoda t 56 container": {1: 0.025},
        "fv217 badger container": {1: 0.025},
        "t95e6 container": {1: 0.025},
        "cs-52 lis container": {1: 0.025},
        "caliban container": {1: 0.025},
        "strv 74a2 container": {1: 0.025},
        "kampfpanzer 50 t container": {1: 0.025},
        "wz-114 container": {1: 0.025},
        "t77 container": {1: 0.025},
        "m-iv-y container": {1: 0.025},
        "lozas sherman container": {1: 0.025},
        "object 907 container": {1: 0.025},
        "annihilator container": {1: 0.025},
        "object 452k container": {1: 0.025},
        "hwk 30 container": {1: 0.025},
        "pawlack container": {1: 0.025}
    },

    "m60 container": {
        "gold": {5000: 1.0}
    },
    "k-91 container": {
        "gold": {1750: 1.0}
    },
    "pudel container": {
        "gold": {750: 1.0}
    },
    "skoda t 45 container": {
        "gold": {1000: 1.0}
    },
    "amx 13 57 container": {
        "gold": {1000: 1.0}
    },
    "astron rex container": {
        "gold": {1500: 1.0}
    },
    "object 260 container": {
        "gold": {5000: 1.0}
    },
    "b-c bourrasque container": {
        "gold": {1500: 1.0}
    },
    "altproto amx 30 container": {
        "gold": {1500: 1.0}
    },
    "tl-7-120 container": {
        "gold": {1750: 1.0}
    },
    "type 64 container": {
        "gold": {750: 1.0}
    },
    "concept 1b container": {
        "gold": {5000: 1.0}
    },
    "bofors tornvagn container": {
        "gold": {1500: 1.0}
    },
    "wz-111 5a container": {
        "gold": {5000: 1.0}
    },
    "smasher container": {
        "gold": {1000: 1.0}
    },
    "t54e2 container": {
        "gold": {1500: 1.0}
    },
    "titan h-nd container": {
        "gold": {1000: 1.0}
    },
    "emil 1951 container": {
        "gold": {1500: 1.0}
    },
    "leo container": {
        "gold": {1000: 1.0}
    },
    "object 268 version 4 container": {
        "gold": {5000: 1.0}
    },
    "bretagne panther container": {
        "gold": {7500: 1.0}
    },
    "skoda t 27 container": {
        "gold": {1500: 1.0}
    },
    "pz iv s container": {
        "gold": {750: 1.0}
    },
    "strv k container": {
        "gold": {5000: 1.0}
    },
    "skoda t 56 container": {
        "gold": {1500: 1.0}
    },
    "fv217 badger container": {
        "gold": {6500: 1.0}
    },
    "t95e6 container": {
        "gold": {5000: 1.0}
    },
    "cs-52 lis container": {
        "gold": {1000: 1.0}
    },
    "caliban container": {
        "gold": {1500: 1.0}
    },
    "strv 74a2 container": {
        "gold": {750: 1.0}
    },
    "kampfpanzer 50 t container": {
        "gold": {5000: 1.0}
    },
    "wz-114 container": {
        "gold": {1750: 1.0}
    },
    "t77 container": {
        "gold": {1500: 1.0}
    },
    "m-iv-y container": {
        "gold": {1500: 1.0}
    },
    "lozas sherman container": {
        "gold": {750: 1.0}
    },
    "object 907 container": {
        "gold": {5000: 1.0}
    },
    "annihilator container": {
        "gold": {1000: 1.0}
    },
    "object 452k container": {
        "gold": {1750: 1.0}
    },
    "hwk 30 container": {
        "gold": {1500: 1.0}
    },
    "pawlack container": {
        "gold": {750: 1.0}
    }
}

with open(Path("crate_calculator/dropchances/grand_surprise_container_dropchances.json"), "w") as file_path:
    json.dump(dropchances_grand_surprise_container, file_path)