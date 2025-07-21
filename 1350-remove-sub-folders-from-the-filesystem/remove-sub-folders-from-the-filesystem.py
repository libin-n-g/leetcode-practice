class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # create trie Then take all prefix without banches.
        root = TrieNode()
        for path in folder:
            node = root
            for folder_sub in path.split("/"):
                if folder_sub.strip() == "":
                    continue
                if folder_sub in node.children:
                    node = node.children[folder_sub]
                    if node.isEndOfWord:
                        break
                else:
                    new_node = TrieNode()
                    node.children[folder_sub] = new_node 
                    node = new_node
            node.isEndOfWord = True
        stack = [(root, "")]
        base_folders = []
        while stack:
            node, curr_path = stack.pop()
            if node.isEndOfWord:
                base_folders.append(curr_path)
                continue
            for folder_sub in node.children:
                stack.append((node.children[folder_sub], f"{curr_path}/{folder_sub}"))
        return base_folders

                    

            

