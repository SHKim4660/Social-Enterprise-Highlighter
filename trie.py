from typing import Dict, Union, Tuple, Any
import json

class Trie:
    def __init__(self):
        self.chars: Dict[str, Trie] = {}
        self.char = ""

    def insert(self, string: str):
        if len(string) >= 2:
            if string[0] not in self.chars.keys():
                self.chars[string[0]] = Trie()

            self.chars[string[0]].insert(string[1:])
        else:
            self.char = string

    def search(self, string: str, match_prefix=False) -> bool:
        if len(string) >= 2:
            if string[0] not in self.chars.keys():
                return False

            return self.chars[string[0]].search(string[1:], match_prefix)

        else:
            return string == self.char or \
                (string in self.chars.keys() and match_prefix)


def serialize(tr: Trie):
    dictionary: Dict[str, Trie] = tr.chars
    result: Any = {}
    for key in dictionary.keys():
        result[key] = serialize(dictionary[key])

    if tr.char != "":
        return [tr.char, result]
    
    return result

def deserialize(data):
    dict = data
    result = Trie()
    
    if type(data) == list:
        result.char = data[0]
        dict = data[1]

    for key in dict.keys():
        result.chars[key] = deserialize(dict[key])

    return result
        
def from_json(dump: str):
    data = json.loads(dump)
    return deserialize(data)

def to_json(tr: Trie):
    return json.dumps(serialize(tr))

if __name__ == "__main__":
    tr = Trie()

    tr.insert("asdf")
    tr.insert("g")
    tr.insert("as")
    tr.insert("각섬석")
    tr.insert("김병만")
    print(tr.search("각섬"))
    print(tr.search("병만"))
    print(tr.search("asdf"))
    print(tr.search("a", match_prefix=True))

    data = serialize(tr)
    print(data)
    print(serialize(deserialize(data)))

    str = to_json(tr)
    print(str)
    print(serialize(from_json(str)))
