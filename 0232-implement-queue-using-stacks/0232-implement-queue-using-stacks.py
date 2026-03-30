class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Always push into in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has the front element
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Ensure out_stack has the front element
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move(self):
        # Transfer elements only when out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())