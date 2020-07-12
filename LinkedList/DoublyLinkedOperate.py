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
