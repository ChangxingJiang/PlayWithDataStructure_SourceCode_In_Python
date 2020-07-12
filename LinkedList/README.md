## SinglyLinkedNode 单链表结点
```python
class SinglyLinkedNode:
    """单链表结点"""

    __slots__ = "value", "next"  # 使用__slots__减少内存占用

    def __init__(self, value, next: "SinglyLinkedNode" = None):
        self.value = value  # 数据域
        self.next = next  # 指针域

    def __str__(self):
        return str(self.value) + "->" + str(self.next)
```

## SinglyLinkedOperate 单链表的基本操作：读取、插入、删除、整表创建

```python
from typing import List

from LinkedList.SinglyLinkedNode import SinglyLinkedNode


# 单链表的读取(给定读取坐标)
def get_node_by_index(head: "SinglyLinkedNode", index: int):
    for _ in range(index + 1):  # 寻找第index个结点(从0开始计数)的前一个结点，如果链表长度不足则不删除
        if not head.next:
            return None
        head = head.next
    else:
        return head.value


# 单链表的添加操作(在给定结点后添加)
def add_node_by_prev(prev: "SinglyLinkedNode", value):
    node = SinglyLinkedNode(value)  # 使用给定值初始化新结点(node)
    node.next = prev.next  # 令新结点(node)指向给定结点(prev)的下一个结点
    prev.next = node  # 令给定结点(prev)指向新结点(node)


# 单链表的添加操作(给定插入坐标)
def add_node_by_index(head: "SinglyLinkedNode", index: int, value):
    idx = -1  # 因为从头结点开始遍历，故使用头结点的坐标-1
    while idx < index and head.next:  # 寻找第index个结点(从0开始计数)，如果链表长度不足则添加在链表尾部
        head = head.next
        idx += 1
    add_node_by_prev(head, value)  # 在第index个结点后添加新结点


# 单链表的删除操作(在给定结点后删除)
def delete_node_by_prev(prev: "SinglyLinkedNode"):
    prev.next = prev.next.next  # 令给定结点(prev)直接指向被删除结点的下一个结点


# 单链表的删除操作(给定删除坐标)
def delete_node_by_index(head: "SinglyLinkedNode", index: int):
    for _ in range(index):  # 寻找第index个结点(从0开始计数)的前一个结点，如果链表长度不足则不删除
        if not head.next:
            break
        head = head.next
    else:
        delete_node_by_prev(head)


# 单链表的整表创建
def build_singly_list_node(values: List):
    node = head = SinglyLinkedNode(None)  # 创建头结点，node指向尾结点（此时即头结点）
    for value in values:
        node.next = SinglyLinkedNode(value)  # 创建新结点，并令当前链表尾部的终端结点指向新结点
        node = node.next  # node重新指向尾结点（即新创建的节点）
    return head
```

## SinglyLinkedList 管理单链表的基本类：读取、插入、删除

```python
from LinkedList.SinglyLinkedNode import SinglyLinkedNode


class SinglyLinkedList:
    """管理单向链表的基本类（使用头结点）"""

    def __init__(self):
        """初始化单向链表"""
        self._head = SinglyLinkedNode(None)  # 创建头结点
        self._size = 0

    def __len__(self):
        """返回链表中元素的数量"""
        return self._size

    def is_empty(self):
        """返回链表是否为空"""
        return self._size == 0

    def get(self, index: int):
        """依据坐标读取变量：返回链表中第index个元素的值"""
        if index < 0 or index >= self._size:
            return -1
        curr = self._head
        for _ in range(index + 1):
            curr = curr.next
        return curr.value

    def add_at_head(self, value):
        """在头结点前添加结点"""
        self.add_at_index(0, value)

    def add_at_tail(self, value):
        """在尾结点之后添加结点"""
        self.add_at_index(self._size, value)

    def add_at_index(self, index: int, value):
        """在指定坐标前添加结点（若坐标无效则不添加）：在链表中第index个元素前插入值为value的结点"""
        if index < 0 or index > self._size:
            return
        self._size += 1
        prev = self._head
        for _ in range(index):
            prev = prev.next
        node = SinglyLinkedNode(value, prev.next)
        prev.next = node

    def delete_at_index(self, index: int):
        """依据坐标删除结点（若坐标无效则不删除）"""
        if index < 0 or index >= self._size:
            return
        self._size -= 1
        prev = self._head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
```

## DoublyLinkedNode 双链表结点

```python
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
```

## DoublyLinkedOperate 双链表的基本操作：插入、删除、整表创建

```python
from typing import List

from LinkedList.DoublyLinkedNode import DoublySimplyListNode


# 双链表的添加操作(在给定结点后添加)
def add_node_by_prev(prev: "DoublySimplyListNode", value):
    node = DoublySimplyListNode(value)  # 使用给定值初始化新结点(node)
    node.prev = prev  # 令新结点(node)的前驱指针指向给定结点(prev)
    node.next = prev.next  # 令新结点(node)的后续指针指向给定结点(prev)的后一个结点

    prev.next = node  # 令给定结点(prev)的后驱指针指向新结点
    node.next.prev = node  # 令后一个节点的前驱指针指向新结点


# 双链表的删除操作(删除给定结点)
def delete_node_by_node(node: "DoublySimplyListNode"):
    node.prev.next, node.next.prev = node.next, node.prev  # 令给定结点前一个结点的后驱指针指向给定结点的后驱结点，后一个结点的前驱指针指向给定结点的前驱结点


# 双链表的整表创建
def build_doubly_list_node(values: List):
    node = head = DoublySimplyListNode(None)  # 创建头结点，node指向尾结点（此时即头结点）
    for value in values:
        new = DoublySimplyListNode(value)  # 创建新结点
        new.prev = node  # 令新结点的前驱指针指向当前节点
        new.next = head  # 令新结点的后继指针指向当前节点

        node.next = new  # 并令当前链表尾部的终端结点指向新结点
        node = node.next  # node重新指向尾结点（即新创建的节点）
    head.prev = node  # 令头结点的前驱指针指向链表尾部的终端结点
    return head
```

## DoublyLinkedList 管理双链表的基本类：插入、删除

```python
from LinkedList.DoublyLinkedNode import DoublySimplyListNode


class DoublyLinkedBase:
    """管理双向链表的基本类（使用双侧哨兵结点）"""

    def __init__(self):
        self._header = DoublySimplyListNode(None)  # 头部哨兵结点
        self._trailer = DoublySimplyListNode(None)  # 尾部哨兵结点
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        """返回链表中元素的数量"""
        return self._size

    def is_empty(self):
        """返回链表是否为空"""
        return self._size == 0

    def insert_between(self, value, prev, next):
        """向链表中添加新结点"""
        node = DoublySimplyListNode(value, prev, next)
        prev.next = node
        next.prev = node
        self._size += 1
        return node

    def delete_node(self, node):
        """从链表中删除结点"""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self._size -= 1
        value = node.value
        node.prev = node.next = node.val = None
        return value
```
