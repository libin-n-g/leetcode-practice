class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def earliestAndLatest(n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
            if firstPlayer > secondPlayer:
                firstPlayer, secondPlayer = secondPlayer, firstPlayer
            firstPlayer = min(firstPlayer, secondPlayer)
            if firstPlayer + secondPlayer == n + 1:
                return [1,1]
            elif n == 4:
                return [2,2]
            elif firstPlayer + secondPlayer > n + 1:
                # MIRROR will produce same result. Will help in CASE 2 as 
                # we do not need to consider case where second player overtakes 
                # first player(in position on line) when we take mirror.
                return earliestAndLatest(n, n - secondPlayer + 1, n - firstPlayer + 1)
            earliest, latest = n, 0
            next_round_count = (n + 1) // 2 # Half of n
            if secondPlayer <= next_round_count:
                # CASE 1: both players are present in First half.
                # firstPlayer - 1 players stand in line before firstPlayer
                for i in range(firstPlayer):
                    # secondPlayer - firstPlayer - 1 players stand in line b/w firstPlayer and secondPlayer
                    for j in range(secondPlayer - firstPlayer):
                        # If we assume recounting players again from 1 to n for next round. 
                        # The position of firstPlayer will be i + 1 (assuming i player before firstPlayer has won)
                        # The position of secondPlayer will be i + 1 + j + 1 (assuming j players b/w first and second player has won)
                        earliest_temp, latest_temp = earliestAndLatest(next_round_count, i + 1, i + j + 2)
                        earliest = min(earliest, earliest_temp)
                        latest = max(latest, latest_temp)
            else:
                # CASE 2: first and second are in opposite half.
                mirrored_second_player =  (n - secondPlayer + 1)  
                # mid = secondPlayer - (n - secondPlayer + 1) plyers who will win b/w 
                mid = (secondPlayer - mirrored_second_player) // 2
                # we do not need to add 1 as mid player(if exists) will be passed to next round
                # firstPlayer - 1 players stand in line before firstPlayer
                for i in range(firstPlayer):
                    # mirrored secondPlayer - firstPlayer - 1 players stand in line b/w firstPlayer and secondPlayer (in next level)
                    for j in range(n - secondPlayer + 1 - firstPlayer):
                        # If we assume recounting players again from 1 to n for next round. 
                        # note that mid plyayers will be in between first and second players always. 
                        # this is because secondPlayer is bigger than mirrored secondPlayer. 
                        # Hence we had to results of mid matches before secondPlayer. 
                        earliest_temp, latest_temp = earliestAndLatest(next_round_count, i + 1, i + j + mid + 2)
                        earliest = min(earliest, earliest_temp)
                        latest = max(latest, latest_temp)
            return [earliest + 1, latest + 1]
        earliest, latest = earliestAndLatest(n, firstPlayer, secondPlayer)
        # earliestAndLatest.cache_clear()
        return [earliest, latest]
        
    def earliestAndLatest_recursive(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        ret = [100, 0]
        def play_game(i, players, current_result, n, round_num):
            # print(i, players, current_result, n, round_num, n//2 + n % 2)
            if i == n-i-1:
                print(i)
                play_game(i+1, players, current_result + [players[i]], n,round_num)
            elif i >= n//2:
                current_result.sort()
                play_game(0, current_result, [] , n//2 + n % 2, round_num + 1)
            elif firstPlayer in [players[i], players[n-i-1]] and secondPlayer in [players[i], players[n-i-1]]:
                ret[1] = max(ret[1], round_num)
                ret[0] = min(ret[0], round_num)
            elif firstPlayer in [players[i], players[n-i-1]]:
                play_game(i+1, players, current_result + [firstPlayer], n,round_num)
            elif secondPlayer in [players[i], players[n-i-1]]:
                play_game(i+1, players, current_result + [secondPlayer], n,round_num)
            else:
                # current_result.append(players[i])
                play_game(i+1, players, current_result + [players[i]], n,round_num)
                # current_result.append(players[n-i-1])
                play_game(i+1, players, current_result + [players[n-i-1]] , n, round_num)
        play_game(0, list(range(1, n+1)), [], n, 1)
        return ret


                    