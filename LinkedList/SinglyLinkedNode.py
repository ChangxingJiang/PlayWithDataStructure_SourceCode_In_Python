class SinglyLinkedNode:
    """单链表结点"""

    __slots__ = "value", "next"  # 使用__slots__减少内存占用

    def __init__(self, value, next: "SinglyLinkedNode" = None):
        self.value = value  # 数据域
        self.next = next  # 指针域

    def __str__(self):
        return str(self.value) + "->" + str(self.next)
