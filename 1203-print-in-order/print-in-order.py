class Foo:
    def __init__(self):
        self.turn = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.turn = 2  # Signal that first is done, allow second

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.turn != 2:  # Wait until first is done
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.turn = 3  # Signal that second is done, allow third

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.turn != 3:  # Wait until second is done
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()