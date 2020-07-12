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
