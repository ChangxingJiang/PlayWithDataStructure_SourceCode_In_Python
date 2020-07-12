from LinkedList.SinglyLinkedNode import SinglyLinkedNode
from Queue.Queue import Queue


class CircularLinkedQueue(Queue):
    """链式存储结构的队列（循环链表）"""

    def __init__(self):
        super().__init__()
        self._tail = None  # 尾指针
        self._size = 0  # 队列的元素数量

    def __len__(self):
        """返回队列中元素的数量"""
        return self._size

    def is_empty(self):
        """返回队列是否为空"""
        return self._size == 0

    def clear(self):
        """将队列清空"""
        self._tail = None  # 尾指针
        self._size = 0  # 队列的元素数量

    def first(self):
        """若队列存在且非空，返回队列的队头元素"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        return self._tail.next.value

    def dequeue(self):
        """删除队列中的队头元素并返回该元素的值"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next  # 令尾结点直接指向原头结点的下一个结点
        self._size -= 1
        return head.value

    def enqueue(self, value):
        """插入新元素value到队列中并成为队尾元素"""
        node = SinglyLinkedNode(value, None)  # 构造链表对象
        if self.is_empty():
            node.next = node
        else:
            node.next = self._tail.next  # 令新结点指向头结点
            self._tail.next = node  # 令原来的尾结点指向新结点
        self._tail = node  # 令尾指针指向新的尾结点（即新结点）
        self._size += 1
