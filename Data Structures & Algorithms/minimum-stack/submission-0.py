class Node:
    def __init__(self, val=None, cur_min=None):
        self.val = val
        self.cur_min = cur_min
        self.next = None


class MinStack:
    def __init__(self):
        self.hd = None

    def push(self, val: int) -> None:
        if not self.hd:
            self.hd = Node(val, val)
        else:
            new_min = min(val, self.hd.cur_min)
            node = Node(val, new_min)
            node.next = self.hd
            self.hd = node

    def pop(self) -> None:
        if self.hd:
            self.hd = self.hd.next

    def top(self) -> int:
        return self.hd.val if self.hd else None

    def getMin(self) -> int:
        return self.hd.cur_min if self.hd else None
