
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        prev = ""
        ans = []
        for f in folder:
            if prev and f.startswith(prev) and f[len(prev)] == "/":
                continue
            ans.append(f)
            prev = f
        return ans


    def removeSubfolders_Trie(self, folder: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}  # Dictionary to store child nodes, keyed by folder name
                self.isEndOfWord = False  # Flag to mark if the node represents the end of a folder path
        # Initialize the root of the Trie
        root = TrieNode()
        
        # Step 1: Build the Trie from the list of folder paths
        for path in folder:
            node = root  # Start at the root for each path
            # Split the path into components (e.g., "/a/b/c" -> ["", "a", "b", "c"])
            for folder_sub in path.split("/"):
                # Skip empty components (e.g., leading/trailing slashes)
                if folder_sub.strip() == "":
                    continue  # Continue to the next component, as empty strings are not valid folder names
                
                # Check if the current folder component exists in the node's children
                if folder_sub in node.children:
                    node = node.children[folder_sub]  # Move to the existing child node
                    # If the current node is marked as the end of a path, this path is a subfolder
                    # of a previously processed folder (e.g., "/a/b" exists, and we're processing "/a/b/c")
                    if node.isEndOfWord:
                        break  # Stop processing this path, as it's a subfolder and won't be included
                else:
                    # Create a new node for this folder component
                    new_node = TrieNode()
                    node.children[folder_sub] = new_node
                    node = new_node  # Move to the new node
            # Mark the final node as the end of a folder path
            node.isEndOfWord = True
        
        # Step 2: Collect base folders (those without subfolders) using a stack-based traversal
        stack = [(root, "")]  # Stack stores tuples of (node, current_path)
        base_folders = []  # List to store the final base folder paths
        
        # Perform a depth-first traversal of the Trie
        while stack:
            node, curr_path = stack.pop()  # Get the current node and its path
            # If this node marks the end of a folder path, add it to the result
            if node.isEndOfWord:
                base_folders.append(curr_path)  # Add the path to the result
                continue  # Skip processing children, as this is a base folder (no need to explore subfolders)
            
            # Add all child nodes to the stack to continue building the path
            for folder_sub in node.children:
                # Construct the path for the child node (e.g., "/a" -> "/a/b")
                stack.append((node.children[folder_sub], f"{curr_path}/{folder_sub}"))
        
        return base_folders  # Return the list of base folders