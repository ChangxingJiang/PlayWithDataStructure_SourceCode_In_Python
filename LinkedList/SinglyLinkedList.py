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
