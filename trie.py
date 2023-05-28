from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        for i in word:
            if i not in current.children.keys():
                current.children[i] = TrieNode()
            current = current.children[i]
        current.endOfString = True

    def search(self,word):
        current = self.root
        for i in word:
            if i not in current.children.keys():
                return False
            current  = current.children[i]
        if current.endOfString:
            return True
        return False

    def start_del(self, index, word, node):
        if len(word) == index:
            if node.endOfString:
                if len(node.children.keys())==1:
                    del node
                    return True
                else:
                    node.endOfString = False
                    return False
            else:
                return False
        elif word[index] in node.children.keys():
            if self.start_del(index+1, word, node.children[word[index]]):
                if len(node.children.keys())==1:
                    del node
                    return True
                else:
                    node.endOfString = False
                    return False

    def delete(self,word):
        current = self.root
        return self.start_del(0, word, current)


trie = Trie()
trie.insert("thunder")
trie.insert("thunderbolt")
trie.insert("thundering")
trie.delete("thunderbolt")
print(trie.search("thunderbolt"))
trie.insert("thunderbolt")
print(trie.search("thunderbolt"))
trie.delete("thunders")
print(trie.search("thunder"))
print(trie.search("thundering"))