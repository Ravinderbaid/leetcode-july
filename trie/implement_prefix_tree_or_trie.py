class Trienode:
    def __init__(self):
        self.childnode = {}
        self.is_end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trienode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for char in word:
            node = curr_node.childnode.get(char, Trienode())
            curr_node.childnode[char] = node
            curr_node = node
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for char in word:
            if curr_node.childnode.get(char):
                curr_node = curr_node.childnode[char]
            else:
                return False
        if curr_node.is_end:
            return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for char in prefix:
            if curr_node.childnode.get(char):
                curr_node = curr_node.childnode[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)