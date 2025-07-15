class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
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


                    