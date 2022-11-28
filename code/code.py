import binascii
import gmpy2
import random
import sys
from gmpy2 import *
from hashlib import md5

sys.setrecursionlimit(100000)


def encrypt_md5(s):  # 数字摘要加密
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))

    # 加密
    return new_md5.hexdigest()


# rs = gmpy2.random_state()


rs = gmpy2.random_state(random.randint(0, 100))


# 生成素数P,Q
def gen_prime():
    p = gmpy2.mpz_urandomb(rs, 1024)  # 随机生成一个0到1024位的素数
    while not gmpy2.is_prime(p):  # 判断是否为质数
        p = gmpy2.mpz_urandomb(rs, 1024)  # 若不是则重新生成
    return p


# 拓展欧几里得算法
def exgcd(a, b):
    if b == 0:
        return 1, 0

    else:
        x, y = exgcd(b, a % b)
        x, y = y, (x - (a // b) * y)
    return x, y


# 生成密钥e,d
def get_e_d(phi):
    e = gmpy2.mpz_random(rs, phi)  # 随机生成比r小的正整数
    while gmpy2.gcd(e, phi) != 1:  # 判断两个数是否互质
        e = gmpy2.mpz_random(rs, phi)  # 随机生成一个0~phi的,与phi互素的数
    d, k = exgcd(e, phi)

    # d = gmpy2.invert(e, phi)
    # print(d)# 生成d
    return e, d


# 对明文加密
def encrypt(plain_text, e, n):
    m = mpz(binascii.hexlify(plain_text.encode('utf-8')), 16)  # 转为16换进制
    cipher_text = gmpy2.powmod(m, e, n)

    return cipher_text


# rsa解密
def decrypt(cipher_text, d, n):
    m = gmpy2.powmod(cipher_text, d, n)
    plain_text = binascii.unhexlify(format(m, 'x')).decode('utf-8')
    return plain_text


if __name__ == "__main__":
    p = gen_prime()
    q = gen_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = get_e_d(phi)
    plain_text = input("请输入明文：")

    plain_text1 = encrypt_md5(plain_text)
    print("加密后的信息摘要是:" + plain_text1)

    cipher_text = encrypt(plain_text1, e, n)
    print("RSA加密后是：%x" % cipher_text)

    plain_text2 = decrypt(cipher_text, d, n)
    print("RSA解密后是：{}".format(plain_text2))

    plain_text3 = encrypt_md5(plain_text)
    if plain_text2 == plain_text3:
        print("信息相同,签名有效")
