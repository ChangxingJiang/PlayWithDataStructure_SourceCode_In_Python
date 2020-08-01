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


if __name__ == "__main__":
    print(get_next("abcdex"))  # [-1, 0, 0, 0, 0, 0]
    print(get_next("abcabx"))  # [-1, 0, 0, 0, 1, 2]
    print(get_next("ababaaaba"))  # [-1, 0, 0, 1, 2, 3, 1, 1, 2]
    print(get_next("aaaaaaaab"))  # [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    print(index_kmp("abcdefgab", "abcdex", 0))  # -1
    print(index_kmp("abcabfgab", "abcabx", 0))  # -1

    print(get_next_val("ababaaaba"))  # [-1, 0, -1, 0, -1, 3, 1, 0, -1]
    print(get_next_val("aaaaaaaab"))  # [-1, -1, -1, -1, -1, -1, -1, -1, 7]

    print(index_kmp_mend("abcdefgab", "abcdex", 0))  # -1
    print(index_kmp_mend("abcabfgab", "abcabx", 0))  # -1
