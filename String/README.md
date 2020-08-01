## 串的抽象数据类型

```python
def str_assign(chars: List[str]):
    """生成一个其值等于字符串常量chars的串"""
    return "".join(chars)


def str_copy(s: str):
    """由串s复制得串t"""
    return copy.deepcopy(s)


def string_empty(s: str):
    """若串s为空，则返回True，否则返回False"""
    return not s


def str_length(s: str):
    """返回串s的元素个数，即串的长度"""
    return len(s)


def concat(s1: str, s2: str):
    """返回s1和s2联接而成的新串"""
    return s1 + s2


def sub_string(s: str, pos: int, length: int):
    """返回串s的第pos个字符起长度为length的子串"""
    if 0 <= pos <= pos + length <= len(s):
        return s[pos: length]


def index(s: str, t: str, pos):
    """若主串s中存在和串t值相同的子串，则返回它在主串s中第pos个字符之后第一次出现的位置，否则返回0"""
    if 0 <= pos < len(s):
        if t in s[pos:]:
            return s[pos:].index(t)
    return 0


def replace(s: str, t: str, v: str):
    """用V替换主串s中出现的所有与t相等的不重叠的子串"""
    return s.replace(t, v)


def str_insert(s: str, pos: int, t: str):
    """在串s的第pos个字符之前插入串t"""
    if 0 <= pos <= len(s):
        return s[:pos] + t + s[pos:]


def str_delete(s: str, pos: int, length: int):
    """在传s中删除第pos个字符起长度为length的子串"""
    if 0 <= pos <= pos + length <= len(s):
        return s[:pos] + s[pos + length:]
```

## 朴素的模式匹配算法

> 时间复杂度：O(N×M)，其中N为字符串s的长度，M为字符串t的长度

```python
def index_simple(s: str, t: str, pos: int):
    """朴素的模式匹配算法"""
    i = pos  # i用于主串s中当前位置下标，若pos不为1则从pos位置开始匹配
    j = 0  # j用于子串t中当前位置下标值
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= len(t):
        return i - len(t)
    else:
        return -1


def index_simple_2(s: str, t: str, pos: int):
    """朴素的模式匹配算法"""
    while pos + len(t) <= len(s):
        if s[pos:pos + len(t)] == t:
            return pos
        pos += 1
    else:
        return -1
```

## KMP模式匹配算法

> 时间复杂度：O(N+M)，其中N为字符串s的长度，M为字符串t的长度

```python
def get_next(t):
    """通过计算返回子串t的next数组"""
    i = 0
    j = -1
    next = [-1] * len(t)
    while i < len(t) - 1:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]  # 若字符不相同，则j值回溯
    return next


def index_kmp(s: str, t: str, pos: int):
    """KMP模式匹配算法"""
    i = pos  # i用于主串s中当前位置下标，若pos不为1则从pos位置开始匹配
    j = 0  # j用于子串t中当前位置下标值
    next = get_next(t)
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j >= len(t):
        return i - len(t)
    else:
        return -1


def get_next_val(t):
    """通过计算返回子串t的next数组(改进算法)"""
    i = 0
    j = -1
    next = [-1] * len(t)
    while i < len(t) - 1:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            if t[i] != t[j]:
                next[i] = j
            else:
                next[i] = next[j]
        else:
            j = next[j]  # 若字符不相同，则j值回溯
    return next


def index_kmp_mend(s: str, t: str, pos: int):
    """KMP模式匹配算法(改进算法)"""
    i = pos  # i用于主串s中当前位置下标，若pos不为1则从pos位置开始匹配
    j = 0  # j用于子串t中当前位置下标值
    next = get_next_val(t)
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j >= len(t):
        return i - len(t)
    else:
        return -1
```