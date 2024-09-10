'''
Simply class that holds all dropchances and exposes a function to get
dropped items and their respective amounts with dropchances 
(as well as a flag if the requested item is a group) for any given item (that is in dropchances)

return strucutre:
    As in json
    groups is used as a by-ref return for possible groups. Currently only determined by item name

(First tuple element could be dict instead of list, need to check implementation for what seems more sensible. 
Ideally the values are returned as disconnected as possible to have little dropchances reading logic 
in the other classes and functions as significant datastructure changes could do away entirely 
with the dict structure, meaning this function would need to create dicts to match the expected return)
'''

class DropchanceReader:
    def __init__(self, dropchances: dict) -> None:
        self.dropchances = dropchances

    # returns container-like dropchances
    def read_dropchance(self, item: str, groups: list|None = None) -> dict:
        if not item in self.dropchances: return {}

        if not groups is None:
            if "group" in item:
                groups[:] = [[key for key in self.dropchances[item]]]
            else:
                groups[:] = [[key] for key in self.dropchances[item]]
        
        return self.dropchances[item]
    
    def read_all_dropchances(self, groups: dict|None = None) -> dict:
        all_dropchances = {}
        for item in self.dropchances:
            item_groups = None
            if groups:
                groups[item] = []
                item_groups = groups[item]

            all_dropchances[item] = self.read_dropchance(item, item_groups)
            
        return all_dropchances