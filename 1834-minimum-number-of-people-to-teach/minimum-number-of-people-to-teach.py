class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Find the minimum number of users who need to learn a new language
        so that all friend pairs can communicate.
      
        Args:
            n: Total number of available languages (1 to n)
            languages: List where languages[i] contains languages known by user i+1
            friendships: List of [user1, user2] pairs representing friendships
      
        Returns:
            Minimum number of users who need to learn a new language
        """
      
        def can_communicate(user1: int, user2: int) -> bool:
            """
            Check if two users can communicate (share at least one common language).
          
            Args:
                user1: First user ID (1-indexed)
                user2: Second user ID (1-indexed)
          
            Returns:
                True if users share a common language, False otherwise
            """
            # Get languages for both users (convert to 0-indexed)
            user1_languages = languages[user1 - 1]
            user2_languages = languages[user2 - 1]
          
            # Check if any language is common between the two users
            for lang1 in user1_languages:
                for lang2 in user2_languages:
                    if lang1 == lang2:
                        return True
            return False
      
        # Find all users who are in friendships that cannot communicate
        users_needing_language = set()
        for user1, user2 in friendships:
            if not can_communicate(user1, user2):
                # Both users in this friendship need to learn a common language
                users_needing_language.add(user1)
                users_needing_language.add(user2)
      
        # Count how many problematic users already know each language
        language_count = Counter()
        for user in users_needing_language:
            # For each user who needs to communicate, count their known languages
            for language_id in languages[user - 1]:
                language_count[language_id] += 1
      
        # The minimum teachings needed is:
        # Total problematic users - Maximum users who already know the same language
        # If we teach the most commonly known language to those who don't know it,
        # we minimize the number of teachings
        if language_count:
            return len(users_needing_language) - max(language_count.values())
        else:
            # If no problematic users exist, no teaching is needed
            return 0