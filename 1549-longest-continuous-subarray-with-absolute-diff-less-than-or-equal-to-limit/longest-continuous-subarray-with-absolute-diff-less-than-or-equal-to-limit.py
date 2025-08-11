class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        motonic_min_stack = deque()
        motonic_max_stack = deque()
        max_size = 1
        left = 0
        for i in range(0, len(nums)):
            while motonic_min_stack and motonic_min_stack[-1] > nums[i]:
                motonic_min_stack.pop()
            while motonic_max_stack and motonic_max_stack[-1] < nums[i]:
                motonic_max_stack.pop()
            motonic_max_stack.append(nums[i])
            motonic_min_stack.append(nums[i])
            # print(left, i, motonic_max_stack, motonic_min_stack)
            while motonic_max_stack and motonic_min_stack and motonic_max_stack[0] - motonic_min_stack[0] > limit:
                # cannot use lese because the left poiner element might have bein already remvoed by monotonic nature
                if nums[left] == motonic_max_stack[0]:
                    motonic_max_stack.popleft()
                if nums[left] == motonic_min_stack[0]:
                    motonic_min_stack.popleft()
                left += 1
            max_size = max(i - left + 1, max_size)
        return max_size