class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_fruit_type = 0
        for f in fruits:
            unplaced = True
            i = 0
            while unplaced and i < len(baskets):
                if baskets[i] >= f:
                    unplaced = False
                    baskets.pop(i)
                else:
                    i+=1
            if unplaced:
                unplaced_fruit_type+=1
        return unplaced_fruit_type

