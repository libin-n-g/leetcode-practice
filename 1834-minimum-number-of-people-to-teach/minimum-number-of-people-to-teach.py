class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        users_need_to_learn = set()
        for u, v in friendships:
            if not languages[u-1] & languages[v-1]:
                # Both users in this friendship need to learn a common language
                users_need_to_learn.add(u-1)
                users_need_to_learn.add(v-1)
        min_count = len(languages)
        for lang in range(1, n+1):
            # Assuming we are going to teach lang to every user who does not know it. 
            count = sum(1 for user in users_need_to_learn if lang not in languages[user])
            min_count = min(count, min_count)
        return min_count
