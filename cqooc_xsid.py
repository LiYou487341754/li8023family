import math
import random
import requests
import ctypes
import hashlib


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shitf(n, i):
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)
# 参数分别是要移的数字和移多少位


def cnonce(v):
    cnon = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    h = ''
    h = h + cnon[unsigned_right_shitf(v, 28) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 24) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 20) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 16) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 12) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 8) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 4) & 0xF]
    h = h + cnon[unsigned_right_shitf(v, 0) & 0xF]
    return h


def nonce():
    url = 'https://www.cqooc.com/user/login'
    headers = {
        "Referer": "https://www.cqooc.com/login?ref=https^%^3A^%^2F^%^2Fwww.cqooc.com^%^2F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko)Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    }
    content = session.get(url=url, headers=headers).json()
    return content['nonce']


def main():
    headers = {
        "Origin": "https://www.cqooc.com",
        "Referer": "https://www.cqooc.com/login?ref=https^%^3A^%^2F^%^2Fwww.cqooc.com^%^2F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    }

    url = "https://www.cqooc.com/user/login"
    params = {
        "username": username,
        "password": password,
        "nonce": nonce(),
        "cnonce": cn
    }
    response = session.post(url=url, headers=headers, params=params).json()
    print(response['xsid'])
    return response['xsid']


if __name__ == "__main__":
    username = input("请输入用户名:")
    password = input("请输入密码:")
    session = requests.session()
    cn = cnonce(math.floor(random.random() * math.pow(2, 32))) + cnonce(math.floor(random.random() * math.pow(2, 32)))
    # 加密
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    pw = nonce() + sha256.hexdigest().upper() + cn
    sha256 = hashlib.sha256()
    sha256.update(pw.encode('utf-8'))
    sha256.hexdigest().upper()
    password = sha256.hexdigest().upper()
    main()
