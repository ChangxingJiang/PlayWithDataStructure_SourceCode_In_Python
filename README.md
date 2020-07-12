# 《大话数据结构》配套源码（Python版）

> 该书随书源码的语言为C；我参考书中内容和配套源码，写了一套Python格式的配套源码。**这套配套源码并非直接翻译C语言的配套源码**，而是结合我的理解略作了修改，这些修改包括：
>
> * 修改变量名的命名由将驼峰式改为下划线式
> * 移除部分Python中不需要手动处理的垃圾回收函数和方法
> * 补充了部分相关的类和函数
>
> 作者：长行
>
> 时间：2020.07.12

## LinkedList  链表  (第3章 - 第2部分)

SinglyLinkedNode 单链表结点

SinglyLinkedOperate 单链表的基本操作：读取、插入、删除、整表创建

SinglyLinkedList 管理单链表的基本类：读取、插入、删除

DoublyLinkedNode 双链表结点

DoublyLinkedOperate 双链表的基本操作：插入、删除、整表创建

DoublyLinkedList 管理双链表的基本类：插入、删除

## Stack  栈  (第4章 - 第1部分)

Stack 栈的结构定义

ArrayStack 顺序存储结构的栈（Python列表存储）

LinkedStack 链式存储结构的栈（单链表存储）

## Queue 队列 (第4章 - 第2部分)

Queue 队列的结构定义

ArrayQueue 顺序存储结构的队列（循环队列）

LinkedQueue 链式存储结构的队列（单链表）

CircularLinkedQueue 链式存储结构的队列（循环链表）





