from LinkedList.SinglyLinkedNode import SinglyLinkedNode
from Stack.Stack import Stack


class LinkedStack(Stack):
    """链式存储结构的栈（单链表存储）"""

    def __init__(self):
        super().__init__()
        self._head = None  # 头指针
        self._size = 0  # 栈中元素的数量

    def __len__(self):
        """返回栈中元素的数量"""
        return self._size

    def is_empty(self):
        """返回栈是否为空"""
        return self._size == 0

    def clear(self):
        """清空栈"""
        self._head = None
        self._size = 0

    def push(self, value):
        """向栈中压入元素"""
        self._head = SinglyLinkedNode(value, self._head)  # 构造链表对象
        self._size += 1

    def top(self):
        """查询栈顶元素"""
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self._head.value

    def pop(self):
        """取出栈顶元素"""
        if self.is_empty():
            raise ValueError("Stack is Empty")
        ans = self._head.value
        self._head = self._head.next
        self._size -= 1
        return ans
