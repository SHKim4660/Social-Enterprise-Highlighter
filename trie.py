from typing import Dict, Union, Tuple, Any
import json

str_ = str

class Trie:
    def __init__(self):
        self.chars: Dict[str, Trie] = {}
        self.char: str = ""

    def insert(self, string: str_) -> None:
        # 두 자 이상
        if len(string) >= 2:
            # 자식 노드로 추가
            if string[0] not in self.chars.keys():
                self.chars[string[0]] = Trie()

            # 재귀 호출
            self.chars[string[0]].insert(string[1:])
        else:
            # 문자열 종결
            self.char = string

    def search(self, string: str, match_prefix=False) -> bool:
        # 두 자 이상
        if len(string) >= 2:
            # 자식 노드 중 없으면 아님
            if string[0] not in self.chars.keys():
                return False

            # 재귀 호출
            return self.chars[string[0]].search(string[1:], match_prefix)

        else:
            # 말단
            return string == self.char or \
                (string in self.chars.keys() and match_prefix) # match_prefix 인 경우만 해당 조건 고려


# 직렬화 포맷: [self.char, self.chars]

# 직렬화
def serialize(tr: Trie):
    dictionary: Dict[str_, Trie] = tr.chars
    result: Any = {}
    # 모든 자식 노드 직렬화
    for key in dictionary.keys():
        result[key] = serialize(dictionary[key])

    if tr.char != "":
        return [tr.char, result]
    
    return result

# 병렬화
def deserialize(data: Any):
    dict = data
    result = Trie()
    
    # 노드이면
    if type(data) == list:
        result.char = data[0]
        dict = data[1]

    # 자식 노드 복원
    for key in dict.keys():
        result.chars[key] = deserialize(dict[key])

    return result
        
# json에서 불러오기
def from_json(dump: str_):
    data: Any = json.loads(dump)
    return deserialize(data)

# json으로 내보내기
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
