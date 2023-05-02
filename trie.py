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

    def search(self, string: str) -> bool:
        if len(string) >= 2:
            if string[0] not in self.chars.keys():
                return False

            return self.chars[string[0]].search(string[1:])

        else:
            if string == self.char:
                return True

            else:
                return False


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

    for i in range():
        tr.insert()

    # tr.insert("asdf")
    # tr.insert("as")
    # tr.insert("각섬석")
    # tr.insert("김병만")
    # print(tr.search("각석"))
    # print(tr.search("병만"))
    # print(tr.search("a"))

    # data = serialize(tr)
    # print(data)
    # print(serialize(deserialize(data)))

    # str = to_json(tr)
    # print(str)
    # print(serialize(from_json(str)))
