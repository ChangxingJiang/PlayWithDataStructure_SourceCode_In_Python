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
