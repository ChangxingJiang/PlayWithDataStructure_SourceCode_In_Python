## Queue 队列的结构定义

```python
class Queue:
    """队列的结构定义"""

    def __init__(self):
        """初始化一个空队列"""
        pass

    def __len__(self):
        """返回队列内元素数量"""
        pass

    def is_empty(self):
        """返回队列是否为空"""
        pass

    def clear(self):
        """将队列清空"""
        pass

    def first(self):
        """若队列存在且非空，返回队列的队头元素"""
        pass

    def dequeue(self):
        """删除队列中的队头元素并返回该元素的值"""
        pass

    def enqueue(self, value):
        """插入新元素value到队列中并成为队尾元素"""
        pass
```

## ArrayQueue 顺序存储结构的队列（循环队列）

```python
class Queue:
    """顺序存储结构的队列（循环队列）"""

    DEFAULT_CAPACITY = 10  # 队列的默认长度（若长度不足则每次扩展到之前的2倍）

    def __init__(self):
        """初始化一个空队列"""
        self._data = [None] * self.DEFAULT_CAPACITY  # 队列存储数组
        self._size = 0  # 队列长度
        self._front = 0  # 队头元素的坐标

    def __len__(self):
        """返回队列内元素数量"""
        return self._size

    def is_empty(self):
        """返回队列是否为空"""
        return self._size == 0

    def clear(self):
        """将队列清空"""
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def first(self):
        """若队列存在且非空，返回队列的队头元素"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        """删除队列中的队头元素并返回该元素的值"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        answer = self._data[self._front]  # 提取队头元素的值
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)  # 计算新的队头元素坐标
        self._size -= 1
        return answer

    def enqueue(self, value):
        """插入新元素value到队列中并成为队尾元素"""
        if self._size == len(self._data):  # 判断队列长度是否超出数组限制
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)  # 计算队尾元素坐标
        self._data[avail] = value
        self._size += 1

    def _resize(self, cap):
        """修改存储队列的数组长度"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):  # 遍历之前的队列
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
```

## LinkedQueue 链式存储结构的队列（单链表）

```python
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
```

## CircularLinkedQueue 链式存储结构的队列（循环链表）

```python
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
```

