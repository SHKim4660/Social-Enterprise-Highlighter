import trie

class SFXTree:
    def __init__(self):
        self.tr = trie.Trie()

    def insert(self, string: str):
        for suffix in [string[i:] for i in range(len(string))]:
            self.tr.insert(suffix)

    def search(self, query: str) -> bool:
        return self.tr.search(query)#, match_prefix=True)

if __name__ == "__main__":
    st = SFXTree()

    st.insert('abcdefg')

    print(st.search("abcdefg"))
    print(st.search("ag"))
