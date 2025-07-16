class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        num_match = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                num_match+=1
                i+=1
            j+=1
            # print(i, j)
        return num_match