class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def earliestAndLatest(n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
            # Ensure firstPlayer has the smaller index to simplify logic
            if firstPlayer > secondPlayer:
                firstPlayer, secondPlayer = secondPlayer, firstPlayer
            
            # Base case: If players are paired directly (opposite positions, e.g., 1 vs n)
            if firstPlayer + secondPlayer == n + 1:
                return [1, 1]
            
            # Base case: For n=4, specific pairing logic (e.g., 1 vs 4, 2 vs 3) results in meeting in round 2
            elif n == 4:
                return [2, 2]
            
            # Symmetry case: If secondPlayer is in the second half, mirror positions
            # This reduces to cases where both players are in the first half or opposite halves
            # Example: firstPlayer = 4, secondPlayer = 9
            # 1, 2, 3, f, 5, 6, 7, 8, s => s, 2, 3, 4, 5, f, 7, 8, 9
            #   new firstPlayer = 1
            #   new secondPlayer = 6
            #   Note that mirror of new second also comes after first. This simplifies CASE 2.
            # Case where both are after mid point is also considered here. 
            # Example: firstPlayer = 4, secondPlayer = 6
            # 1, 2, 3, f, 5, s => s, 2, f, 4, 5, 6
            # new firstPlayer = 1, new econdPlayer = 3
            elif firstPlayer + secondPlayer > n + 1:
                return earliestAndLatest(n, n - secondPlayer + 1, n - firstPlayer + 1)
            
            # Initialize earliest and latest rounds for the current subproblem
            earliest, latest = n, 0
            
            # Calculate the number of players in the next round (ceiling of n/2)
            next_round_count = (n + 1) // 2
            
            # CASE 1: Both players are in the first half of the current round
            if secondPlayer <= next_round_count:
                # Iterate over possible winners before firstPlayer
                # Example: If firstPlayer=2, try i=0,1 (0 or 1 winners before player 2)
                for i in range(firstPlayer):
                    # Iterate over possible winners between firstPlayer and secondPlayer
                    # Example: If secondPlayer=3, firstPlayer=1, try j=0,1 (0 or 1 winners between)
                    for j in range(secondPlayer - firstPlayer):
                        # In the next round, players are renumbered:
                        # - firstPlayer’s position becomes i + 1 (i winners before)
                        # - secondPlayer’s position becomes i + j + 2 (j winners between, plus firstPlayer)
                        # Example: Not executed for n=5, firstPlayer=2, secondPlayer=4
                        earliest_temp, latest_temp = earliestAndLatest(next_round_count, i + 1, i + j + 2)
                        earliest = min(earliest, earliest_temp)
                        latest = max(latest, latest_temp)
            else:
                # CASE 2: firstPlayer in first half, secondPlayer in second half
                
                # Mirror secondPlayer’s position.
                mirrored_second_player = n - secondPlayer + 1
                
                # Calculate the number of players between mirrored_second_player and secondPlayer
                # These players (if any) always advance due to their position. 
                # Example: mid is 5, mirrored second player is 3
                # f, 2, 3, 4, 5, 6, s, 8, 9
                # After playing this round
                # f(=1), _(=2/8), (s=7), _(=6/4),_ (=5) 
                # f, _(may or may not be present), (_, _)(mid values after 7 in above) (7) ...  
                mid = (secondPlayer - mirrored_second_player) // 2
                
                # Iterate over possible winners before firstPlayer
                # Example: firstPlayer=2, so i=0,1
                for i in range(firstPlayer):
                    # Iterate over possible winners between firstPlayer and mirrored secondPlayer
                    # Example: n - secondPlayer + 1 - firstPlayer = 5 - 4 + 1 - 2 = 0, so j=0
                    for j in range(n - secondPlayer + 1 - firstPlayer):
                        # In the next round, players are renumbered:
                        # - firstPlayer’s position becomes i + 1
                        # - secondPlayer’s position accounts for mid players advancing
                        # Example: For i=0, j=0: firstPlayer=0+1=1, secondPlayer=0+0+1+2=3
                        # Call earliestAndLatest(3, 1, 3)
                        earliest_temp, latest_temp = earliestAndLatest(next_round_count, i + 1, i + j + mid + 2)
                        earliest = min(earliest, earliest_temp)
                        latest = max(latest, latest_temp)
            
            # Increment rounds to account for the current round
            # Example: Return [earliest + 1, latest + 1]
            return [earliest + 1, latest + 1]
        
        # Example: Call earliestAndLatest(5, 2, 4)
        # Compute result, clear cache, and return
        earliest, latest = earliestAndLatest(n, firstPlayer, secondPlayer)
        earliestAndLatest.cache_clear()
        return [earliest, latest]

    def earliestAndLatest_recursive(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # Initialize return values: earliest (set high) and latest (set low)
        ret = [100, 0]
        
        def play_game(i, players, current_result, n, round_num):
            # Base case: If index i meets its mirror (n-i-1), only one can advance
            if i == n - i - 1:
                play_game(i + 1, players, current_result + [players[i]], n, round_num)
            # Base case: If we’ve processed half the players, move to the next round
            elif i >= n // 2:
                # Sort the current winners to prepare for the next round
                current_result.sort()
                # Start a new round with the winners
                play_game(0, current_result, [], n // 2 + n % 2, round_num + 1)
            # If firstPlayer and secondPlayer are paired in this round
            elif firstPlayer in [players[i], players[n - i - 1]] and secondPlayer in [players[i], players[n - i - 1]]:
                # They meet, so update earliest and latest rounds
                ret[1] = max(ret[1], round_num)
                ret[0] = min(ret[0], round_num)
            # If only firstPlayer is in the current pair
            elif firstPlayer in [players[i], players[n - i - 1]]:
                # Let firstPlayer advance and continue
                play_game(i + 1, players, current_result + [firstPlayer], n, round_num)
            # If only secondPlayer is in the current pair
            elif secondPlayer in [players[i], players[n - i - 1]]:
                # Let secondPlayer advance and continue
                play_game(i + 1, players, current_result + [secondPlayer], n, round_num)
            else:
                # Neither player is in the pair, try both possible winners
                # Try the left player advancing
                play_game(i + 1, players, current_result + [players[i]], n, round_num)
                # Try the right player advancing
                play_game(i + 1, players, current_result + [players[n - i - 1]], n, round_num)
        
        # Start the game with players numbered 1 to n
        play_game(0, list(range(1, n + 1)), [], n, 1)
        return ret