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
