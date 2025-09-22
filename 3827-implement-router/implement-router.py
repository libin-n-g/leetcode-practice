class Router:

    def __init__(self, memoryLimit: int):
       self.queue = deque(maxlen=memoryLimit)
       self.present = set()
       self.memoryLimit = memoryLimit
       self.count = 0
       self.destination_mapping = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.present:
            return False
        if self.count >= self.memoryLimit:
            s, d, t = self.queue.popleft()
            self.present.remove((s, d, t))
            self.destination_mapping[d].popleft()
            self.count -= 1
        self.queue.append((source, destination, timestamp))
        self.present.add((source, destination, timestamp))
        self.destination_mapping[destination].append(timestamp)
        self.count += 1
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []
        s, d, t = self.queue.popleft()
        self.present.remove((s, d, t))
        self.destination_mapping[d].popleft()
        self.count -= 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lowerBound = bisect.bisect_left(self.destination_mapping[destination], startTime, 0)
        upperBound = bisect.bisect_right(self.destination_mapping[destination], endTime, 0)   
        return upperBound - lowerBound


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)