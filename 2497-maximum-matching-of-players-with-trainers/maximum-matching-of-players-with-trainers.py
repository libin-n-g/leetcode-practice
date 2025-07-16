class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        n = len(players)
        num_match = 0
        for trainer_value in trainers:
            if trainer_value >= players[j]:
                num_match+=1
                j+=1
            if j >= n:
                break

        # players.sort()
        # trainers.sort()
        # i = 0
        # j = 0
        # num_match = 0
        # while i < len(players) and j < len(trainers):
        #     if players[i] <= trainers[j]:
        #         num_match+=1
        #         i+=1
        #     j+=1
        return num_match