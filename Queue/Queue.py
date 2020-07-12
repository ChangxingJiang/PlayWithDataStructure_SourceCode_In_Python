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
