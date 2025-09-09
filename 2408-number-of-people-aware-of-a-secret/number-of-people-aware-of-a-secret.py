class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        count_knowing_secret = 0
        MOD = 10**9 + 7
        people_knowing_secret = defaultdict(int)
        new_people_each_day = defaultdict(int)
        new_people_each_day[1] = 1
        for day in range(1, n+1):
            if new_people_each_day[day] > 0:
                people_knowing_secret[day] += new_people_each_day[day]
                people_knowing_secret[day + forget] -= new_people_each_day[day]
                for d in range(day + delay, day + forget):
                    new_people_each_day[d] += new_people_each_day[day]
            count_knowing_secret = (count_knowing_secret + people_knowing_secret[day]) % MOD
        return count_knowing_secret
        
        # MOD = 10**9 + 7
        # queue = deque([(1, 1)]) # person, days
        # person_count = 1
        # forget_count = 0
        # while queue:
        #     person, day = queue.popleft()
        #     print("parent", person, day)
        #     for d in range(delay, forget):
        #         if day + d <= n:
        #             person_count = (person_count + 1) % MOD
        #             print("child", person_count, day+d)
        #             queue.append((person_count, day+d))
        #     if day + forget <= n:
        #         forget_count = (forget_count + 1) % MOD
        # return (person_count - forget_count) % MOD
