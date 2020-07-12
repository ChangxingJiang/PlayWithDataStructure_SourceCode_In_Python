class DoublySimplyListNode:
    """双链表结点"""

    __slots__ = "value", "next", "prev"  # 使用__slots__减少内存占用

    def __init__(self, value, next: "DoublySimplyListNode" = None, prev: "DoublySimplyListNode" = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        if self.next and self.next.value:
            return str(self.value) + "<->" + str(self.value)
        else:
            return str(self.value) + "<->" + "None"
