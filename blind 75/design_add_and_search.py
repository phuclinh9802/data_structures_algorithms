class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word):
        # use dfs if "." exists
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endOfWord

