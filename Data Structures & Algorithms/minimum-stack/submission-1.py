

class MinStack:
    class Node:
        def __init__(self, val, cur_min, next_node=None):
            self.val = val
            self.cur_min = cur_min
            self.next = next_node

    def __init__(self):
        self.hd = None

    def push(self, val: int) -> None:
        if self.hd is None:
            self.hd = self.Node(val, val)
        else:
            cur_min = min(val, self.hd.cur_min)
            self.hd = self.Node(val, cur_min, self.hd)
            

    def pop(self) -> None:
        self.hd = self.hd.next

    def top(self) -> int:
        return self.hd.val

    def getMin(self) -> int:
        return self.hd.cur_min
