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
