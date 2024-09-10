from pathlib import Path
import json


class DropchanceGetter:

    def __init__(self) -> None:
        json_dropchances_awesome_container_file = open(Path("crate_calculator/dropchances/awesome_container_dropchances.json"))
        dropchances_awesome_container = json.loads(json_dropchances_awesome_container_file.read())

        json_dropchances_black_boxes_file = open(Path("crate_calculator/dropchances/black_box_dropchances.json"))
        dropchances_black_boxes = json.loads(json_dropchances_black_boxes_file.read())

        json_dropchances_collect_em_all_container_file = open(Path("crate_calculator/dropchances/collect_em_all_container_dropchances.json"))
        dropchances_collect_em_all_container = json.loads(json_dropchances_collect_em_all_container_file.read())

        json_dropchances_grand_surprise_container_file = open(Path("crate_calculator/dropchances/grand_surprise_container_dropchances.json"))
        dropchances_grand_surprise_container = json.loads(json_dropchances_grand_surprise_container_file.read())

        json_dropchances_mega_container_file = open(Path("crate_calculator/dropchances/mega_container_dropchances.json"))
        dropchances_mega_container = json.loads(json_dropchances_mega_container_file.read())

        json_dropchances_mystery_boxes_file = open(Path("crate_calculator/dropchances/mystery_box_dropchances.json"))
        dropchances_mystery_boxes = json.loads(json_dropchances_mystery_boxes_file.read())

        json_dropchances_massive_container_file = open(Path("crate_calculator/dropchances/massive_container_dropchances.json"))
        dropchances_massive_container = json.loads(json_dropchances_massive_container_file.read())

        self.crates = [
            (["awesome container", "awesome container group container"], dropchances_awesome_container), 
            (["black box i",  "black box ii", "black box iii", "black box iv", "black box v", 
            "black box vi", "black box vii", "black box viii", "black box ix", "black box x", 
            "black certificate"], dropchances_black_boxes), 
            (["collect em all container"], dropchances_collect_em_all_container), 
            (["grand surprise container", "m60 container", "k-91 container", "pudel container", "skoda t 45 container", 
            "amx 13 57 container", "astron rex container", "object 260 container", "b-c bourrasque container", "altproto amx 30 container", 
            "tl-7-120 container", "type 64 container", "concept 1b container", "bofors tornvagn container", "wz-111 5a container", 
            "smasher container", "t54e2 container", "titan h-nd container", "emil 1951 container", "leo container", 
            "object 268 version 4 container", "bretagne panther container", "skoda t 27 container", "pz iv s container", "strv k container", 
            "skoda t 56 container", "fv217 badger container", "t95e6 container", "cs-52 lis container", "caliban container", 
            "strv 74a2 container", "kampfpanzer 50 t container", "wz-114 container", "t77 container", "m-iv-y container", 
            "lozas sherman container", "object 907 container", "annihilator container", "object 452k container", "hwk 30 container", 
            "pawlack container"], dropchances_grand_surprise_container), 
            (["mega container"], dropchances_mega_container), 
            (["mystery box i", "mystery box ii", "mystery box iii", "mystery certificate"], dropchances_mystery_boxes),
            (["massive container", "massive container group container", "massive container group quest"], dropchances_massive_container)
        ]

        self.non_crates = [
            "gold",
            "gold booster",
            "premium account",
            "lockbox key",
            "gold charm 7",
            "gold charm 10",
            "shining crown animated avatar",
            "riches vault profile background",
            "mystery profile background",
            "lightning catcher animated avatar",
            "massive background"
        ]


    def load_item_dropchances_with_dependencies(self, item: str, dropchances: dict = {}) -> dict:
        if item in self.non_crates: return {}
        if item in dropchances: return {}

        for included_crates, dropchance_collection in self.crates:
            if item in included_crates:
                dropchances |= dropchance_collection

                for loaded_item in dropchance_collection:
                    for loaded_item_drop in dropchance_collection[loaded_item]:
                        dropchances |= self.load_item_dropchances_with_dependencies(loaded_item_drop, dropchances)

        if not item in dropchances: return {}
        return dropchances
