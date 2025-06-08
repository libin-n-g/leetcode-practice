class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def traverse_node(prev):
            ret = []
            value = prev*10
            if 0 < value <= n:
                ret.append(value)
                ret = ret + traverse_node(value)
            for num in range(1, 10):
                value = prev*10 + num
                # print(value)
                if value <= n:
                    ret.append(value)
                else:
                    break
                ret = ret + traverse_node(value)
            return ret 
        return traverse_node(0)