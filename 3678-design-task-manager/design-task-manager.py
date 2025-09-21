class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.priority_heap = []
        self.task_info = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heappush(self.priority_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_info[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.task_info.pop(taskId)
            
    def execTop(self) -> int:
        executing_user = -1
        while self.priority_heap:
            priority, taskId = heappop(self.priority_heap)
            if -taskId in self.task_info and self.task_info[-taskId][1] == -priority:
                executing_user, _ = self.task_info.pop(-taskId)
                return executing_user
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()