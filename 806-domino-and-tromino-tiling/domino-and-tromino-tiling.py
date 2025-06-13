class Solution:
    def numTilings(self, n: int) -> int:
        FF, F = 1, 1 
        # Full[n] = Full[n-1] (vertical domino) 
        # + Full[n-2] (two horizontal domino) +
        # TopMissing[n-1] (tromino)
        # BotomMissing[n-1] (tromino)
        T = 0
        B = 0
        for _ in range(2, n+1):
            FF, F, T, B = F, F + FF + T + B, B + FF, T + FF
            # TopMissing[n] = BottomMissing[n-1] (add horozontal domino)
            # + Full[n-2]
            # print(i, Full_n_1, Full_n, TopMissing, BottomMissing)
            # BottomMissing[n] = TopMissing[n-1] (add horozontal domino)
            # + Full[n-2]
        return F % (10**9 + 7)
        # mod = 10**9 + 7
        # dp = [[None]*(4) for _ in range(n)]
        # def make_state(t1, t2):
        #     state = 0
        #     if t1: state |= 0b01
        #     if t2: state |= 0b10
        #     return state
        # def fill_tile(i, t1, t2):
        #     if i == n:
        #         return 1
        #     state = make_state(t1, t2)
        #     t3 = t4 = i < n -1
        #     if dp[i][state] is not None:
        #         return dp[i][state]
        #     count = 0
        #     if t1 & t2:
        #         # fill vertcal domino once
        #         count += fill_tile(i+1, True, True)
        #         if t3:
        #             # fill tromino case 1
        #             count += fill_tile(i+1, False, True)
        #         if t4:
        #             # fill tromino case 2
        #             count += fill_tile(i+1, True, False)
        #         if t3 and t4:
        #             # fill two domino horizontally
        #             count += fill_tile(i+1, False, False)
        #     if t1 and (not t2):
        #         if t3 and t4:
        #             # Fill using tromino
        #             count += fill_tile(i+1, False, False)
        #         if t4:
        #             # fill using domino horizontally
        #             count += fill_tile(i+1, True, False)
        #     if (not t1) and t2:
        #         if t3 and t4:
        #             # fill using tromino
        #             count += fill_tile(i+1, False, False)
        #         if t3:
        #             # fill using domino horizontally
        #             count += fill_tile(i+1, False, True)
        #     if (not t2) and (not t1):
        #         # skip as it is already filled
        #         count += fill_tile(i+1, True, True)
        #     count = count % mod
        #     dp[i][state] = count
        #     return count 
        # return fill_tile(0, True, True)
