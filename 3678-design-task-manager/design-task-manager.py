from typing import List
from sortedcontainers import SortedList


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        """
        Initialize the TaskManager with a list of tasks.
        Each task is represented as [userId, taskId, priority].
        """
        # Dictionary to store task information: taskId -> (userId, priority)
        self.task_info = {}
      
        # SortedList to maintain tasks ordered by priority (highest first) and taskId (highest first)
        # Using negative values to achieve descending order
        self.priority_queue = SortedList()
      
        # Add all initial tasks
        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Add a new task to the system.
      
        Args:
            userId: ID of the user who owns the task
            taskId: Unique identifier for the task
            priority: Priority level of the task (higher value = higher priority)
        """
        # Store task information in dictionary
        self.task_info[taskId] = (userId, priority)
      
        # Add to sorted list with negative values for descending order
        # Negative priority ensures higher priorities come first
        # Negative taskId ensures higher taskIds come first when priorities are equal
        self.priority_queue.add((-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Edit the priority of an existing task.
      
        Args:
            taskId: ID of the task to edit
            newPriority: New priority value for the task
        """
        # Retrieve current task information
        user_id, old_priority = self.task_info[taskId]
      
        # Remove old entry from sorted list
        self.priority_queue.discard((-old_priority, -taskId))
      
        # Update task information with new priority
        self.task_info[taskId] = (user_id, newPriority)
      
        # Add updated entry to sorted list
        self.priority_queue.add((-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        """
        Remove a task from the system.
      
        Args:
            taskId: ID of the task to remove
        """
        # Retrieve task priority for removal from sorted list
        _, priority = self.task_info[taskId]
      
        # Remove task from dictionary
        self.task_info.pop(taskId)
      
        # Remove task from sorted list
        self.priority_queue.remove((-priority, -taskId))

    def execTop(self) -> int:
        """
        Execute the highest priority task and remove it from the system.
      
        Returns:
            The userId of the executed task, or -1 if no tasks exist
        """
        # Check if there are any tasks to execute
        if not self.priority_queue:
            return -1
      
        # Pop the highest priority task (first element in sorted list)
        # Extract taskId by negating the second element of the tuple
        task_id = -self.priority_queue.pop(0)[1]
      
        # Get the userId of the task owner
        user_id, _ = self.task_info[task_id]
      
        # Remove task from dictionary
        self.task_info.pop(task_id)
      
        return user_id

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()