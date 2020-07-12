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
