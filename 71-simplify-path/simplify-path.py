class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path_list = []
        for x in path.split('/'):
            if x == '.' or x == '':
                continue
            elif x == '..':
                if new_path_list: new_path_list.pop()
            else:
                new_path_list.append(x)
        return '/' + '/'.join(new_path_list)