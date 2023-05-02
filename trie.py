from typing import Dict, Union, Tuple, Any
import json

class Trie:
    def __init__(self):
        self.chars: Dict[js, Trie] = {}
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
    dictionary: Dict[js, Trie] = tr.chars
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
    import random
    import time
    import uuid
    
    tr = Trie()

    tr.insert("asdf")
    tr.insert("as")
    tr.insert("각섬석")
    tr.insert("김병만")
    print(tr.search("as"))
    print(tr.search("asdf"))
    print(tr.search("a"))

    data = serialize(tr)
    print(data)
    print(serialize(deserialize(data)))

    js = to_json(tr)
    print(js)
    print(serialize(from_json(js)))

    benchmark_amount = 100000
    data = []
    for i in range(benchmark_amount):
        data.append(str(uuid.uuid4()))

    trie = Trie()
    for string in data:
        trie.insert(string)

    query = data[:]
    random.shuffle(query)

    randomquery = []
    for i in range(benchmark_amount):
        randomquery.append(str(uuid.uuid4()))

    print("벤치마크 1: 쿼리가 데이터에 있을때")
    print("트라이 사용")
    stime = time.time()
    dummy = None
    for q in query:
        dummy = trie.search(q)
    etime = time.time()

    print(etime - stime, "초", dummy)
    print("트라이 없이")
    stime = time.time()
    dummy = None
    for q in query:
        dummy = q in data

    etime = time.time()
    print(etime - stime, "초", dummy)

    print("벤치마크 2: (대부분의) 쿼리가 데이터에 없을때")
    print("트라이 사용")
    stime = time.time()
    dummy = None
    for q in randomquery:
        dummy = trie.search(q)
    etime = time.time()
    print(etime - stime, "초", dummy)

    print("트라이 없이")
    stime = time.time()
    dummy = None
    for q in randomquery:
        dummy = q in data
    etime = time.time()
    print(etime - stime, "초", dummy)
