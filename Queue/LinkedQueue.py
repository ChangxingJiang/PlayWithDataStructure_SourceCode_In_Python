from LinkedList.SinglyLinkedNode import SinglyLinkedNode
from Queue.Queue import Queue


class LinkedQueue(Queue):
    """链式存储结构的队列（单链表）"""

    def __init__(self):
        super().__init__()
        self._head = None  # 头指针
        self._tail = None  # 尾指针
        self._size = 0  # 队列中元素的数量

    def __len__(self):
        """返回队列中元素的数量"""
        return self._size

    def is_empty(self):
        """返回队列是否为空"""
        return self._size == 0

    def clear(self):
        """将队列清空"""
        self._head = None
        self._tail = None
        self._size = 0

    def first(self):
        """若队列存在且非空，返回队列的队头元素"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        return self._head.value

    def dequeue(self):
        """删除队列中的队头元素并返回该元素的值"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        ans = self._head.value
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans

    def enqueue(self, value):
        """插入新元素value到队列中并成为队尾元素"""
        node = SinglyLinkedNode(value)  # 构造链表对象
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1
