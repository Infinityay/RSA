# Demonstration

## Home Page

![image-20221129105842939](README/image-20221129105842939.png)

## Simulate the RSA encryption and decryption process:

### Step 1	 Input plainText

![image-20221130174916924](README/image-20221130174916924.png)

Then the program will encode it by UTF-8 as:

![image-20221130174900263](README/image-20221130174900263.png)

:x:**Error:** If you forget to input plainText:

![image-20221130174951317](README/image-20221130174951317.png)

### Step 2	Generate primes

You have **two choice**:

1. Generate the two primes with **RSA-2048**:star:(recommened):

![image-20221130175043997](README/image-20221130175043997.png)

2. input the two primes **by hand:**

   ![加载失败](README/image-20221130180156546.png)

   :bangbang: If you choose this way, ensure that the two numbers are primes and $n = p \times q > length(encode(plainText))$, if not, you will get some errors like

   ![加载失败](README/image-20221130180404284.png)

   ![加载失败](README/image-20221130180423220.png)

   ![加载失败](README/image-20221130180431747.png)

### Step 3	Key length

Compute the length of key $n$ and Euler funciton $\varphi(n)$ as: 

![image-20221130175729794](README/image-20221130175729794.png)

:bangbang: **Remember**：you must generate two primes $p$ and $q$ first, or the program will give you an error like this:

![image-20221130175847221](README/image-20221130175847221.png)

### Step 4,  5, 6	Public exponent $e$ and Private exponent $d$ and Keys

![image-20221130180922075](README/image-20221130180922075.png)

### Step 7	Encrypt 

Use publicKey to encrypt $encode(plainText)$ as: $C = M^e $ $mod$ $n$

![image-20221130181432297](README/image-20221130181432297.png)

### Step 8	Decrypt

Use privateKey to decrypt  $C$  as: $M = C^d $ $mod$ $n$

![image-20221130181442594](README/image-20221130181442594.png)

### Step 9	Decode plainText

![image-20221130181409404](README/image-20221130181409404.png)



## Simulate the RSA signature and verification process:

![image-20221129105904851](README/image-20221129105904851.png)

**A Completed Demo for RSA signature:**

First, the sender inputs "hello, world" in the plainText box, clicks the "hash" button, and generates a 128 bit information digest through the MD5 algorithm.

Next, the sender clicks the "get" button to generate the public key and private key through the RSA encryption algorithm. Then the sender clicks the "signature" button to encrypt the information summary. And he transmits the encrypted information to the receiver.

The receiver decrypts the received encrypted message digest to obtain the sender's message digest, then he can input the received plaintext "hello, world" in the plainText box, click the "hash" button, and generate a 128 bit message digest again.

After that, the sender clicks the "verify" button to compare it with the sender's information digest. If it is identical, the information is indeed sent by the sender and has not been tampered with.

## **Announcement:**

> This GUI evolved from [Wanderson-Magalhaes/Simple_PySide_Base](https://github.com/Wanderson-Magalhaes/Simple_PySide_Base)

## More details:

[RSA&Signature (shimo.im)](https://shimo.im/docs/rp3OVdRdRyF0abAm)

[RSA算法三部曲（一） – 生有涯知无涯 (infinityday.cn)](https://www.infinityday.cn/index.php/2022/11/28/rsa算法三部曲（一）/)

