class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if len(flowerbed) > 1 and flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        for i in range(len(flowerbed)-2):
            if flowerbed[i] == flowerbed[i+1] == flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                n -= 1
        if len(flowerbed) > 1 and flowerbed[-2] == flowerbed[-1] == 0:
            flowerbed[-1] = 1
            n -= 1
        return (n <= 0)