class Node:
    def __init__(self, start, end, red=False):
        self.start = start
        self.end = end
        self.right = None
        self.left = None
        self.red = red
    def insert(self, startTime, endTime):
        curr = self
        while True:
            if startTime >= curr.end:
                if not curr.right:
                    curr.right = Node(startTime, endTime, not curr.red)
                    return True
                curr = curr.right
            elif endTime <= curr.start:
                if not curr.left:
                    curr.left = Node(startTime, endTime, not curr.red)
                    return True
                curr = curr.left
            else:
                return False
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = Node(startTime, endTime)
        else:
            return self.root.insert(startTime, endTime)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)