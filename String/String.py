import copy
from typing import List


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
