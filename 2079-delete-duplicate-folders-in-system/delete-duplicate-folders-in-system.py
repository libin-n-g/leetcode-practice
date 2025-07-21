class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.end = False
                self.deleted = False
        root = TrieNode()
        for path in paths:
            curr_node = root
            for f in path:
                new_node = curr_node.children.get(f)
                if new_node is None:
                    new_node = curr_node.children[f] = TrieNode()
                curr_node = new_node
            curr_node.end =True
        node_map = {}
        def hash_tree(node, key):
            hashes = []
            for f in sorted(node.children.keys()):
                hashes.append(f"{f},{hash_tree(node.children[f], f)}")
            hash_key = f"[{']['.join(hashes)}]"
            if hash_key in node_map:
                print(hash_key, "deleted", key)
                node_map[hash_key].deleted = True
                node.deleted = True
            if len(hashes) != 0:
                node_map[hash_key] = node
            # print(hash_key, node.children)
            return hash_key
        hash_tree(root, "")
        # print(node_map)
        ret = []
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            print(path)
            if node.deleted:
                continue
            else:
                if path: ret.append(path)
            for f in node.children:
                stack.append((node.children[f], path + [f]))
        return ret
                