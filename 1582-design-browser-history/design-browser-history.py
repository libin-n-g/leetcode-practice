class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = -1
    def visit(self, url: str) -> None:
        while self.current_index != -1:
            self.history.pop()
            self.current_index += 1
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_index = max(self.current_index - steps,  -len(self.history))
        print(self.current_index, len(self.history), steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(self.current_index + steps, -1)
        return self.history[self.current_index]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)