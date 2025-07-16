class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort players in ascending order to start with the smallest skill requirements
        players.sort()
        # Sort trainers in ascending order to start with the smallest training capacities
        trainers.sort()
        # Initialize pointer j to track the current player index
        j = 0
        # Get the total number of players
        n = len(players)
        # Initialize counter for the number of successful matches
        num_match = 0
        
        # Iterate through each trainer’s capacity
        for trainer_value in trainers:
            # Check if the current trainer’s capacity is sufficient for the current player’s skill
            # and if there are still players left to match
            if j < n and trainer_value >= players[j]:
                # Increment the match count since the trainer can train this player
                num_match += 1
                # Move to the next player
                j += 1
                # If all players have been matched, return the current number of matches
                if j >= n:
                    return num_match
        
        # Return the total number of matches found
        return num_match