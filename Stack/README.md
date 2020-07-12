## Stack 栈的结构定义

```python
class Stack:
    """栈的结构定义"""

    def __init__(self):
        """初始化一个空栈"""
        pass

    def __len__(self):
        """返回栈内元素数量"""
        pass

    def is_empty(self):
        """返回栈是否为空栈"""
        pass

    def clear(self):
        """清空栈"""
        pass

    def top(self):
        """若栈存在且非空，则返回栈顶元素"""
        pass

    def push(self, value):
        """若栈存在，则插入新元素value到栈中并成为栈顶元素"""
        pass

    def pop(self):
        """若栈存在，则删除栈顶元素并返回其值"""
        pass
```

## ArrayStack 顺序存储结构的栈（Python列表存储）

```python
from Stack.Stack import Stack


class ArrayStack(Stack):
    """顺序存储结构的栈（Python列表存储）"""

    def __init__(self):
        """初始化一个空栈"""
        super().__init__()
        self._data = []

    def __len__(self):
        """返回栈内元素数量"""
        return len(self._data)

    def is_empty(self):
        """返回栈是否为空栈"""
        return len(self._data) == 0

    def clear(self):
        """清空栈"""
        self._data.clear()

    def top(self):
        """若栈存在且非空，则返回栈顶元素"""
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self._data[-1]

    def push(self, value):
        """若栈存在，则插入新元素value到栈中并成为栈顶元素"""
        self._data.append(value)

    def pop(self):
        """若栈存在，则删除栈顶元素并返回其值"""
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self._data.pop()
```

## LinkedStack 链式存储结构的栈（单链表存储）

[SinglyLinkedNode(单链表结点)](https://dataartist.blog.csdn.net/article/details/107294965)

```python
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
```