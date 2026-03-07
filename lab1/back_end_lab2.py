import struct
import math


def padding(raw_text):
    buffer = bytearray(raw_text.encode('utf-8'))
    length = len(buffer) * 8
    buffer.append(0x80)

    padd_length = (56 - len(buffer) % 64) % 64

    buffer.extend(b'\x00' * padd_length)

    buffer.extend(struct.pack('<Q', length))

    return buffer

def MD5(input_data):

    words_array = []
    temp = 0
    for i in range(len(input_data)):
        temp |= input_data[i] << (i % 4) * 8
        if (i + 1) % 4 == 0:
            words_array.append(temp)
            temp = 0

    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    a, b, c, d = A, B, C, D


    def combine(A, B, C, D, i, words_array):

        currentIndex = -1
        if 0 <= i < 16:
            currentIndex = i % 16
        elif 16 <= i < 32:
            currentIndex = (5*i + 1) % 16
        elif 32 <= i < 48:
            currentIndex = (3 * i + 5) % 16
        elif 48 <= i < 64:
            currentIndex = (7*i) % 16
            
        T = int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF
        S = [7, 12, 17, 22] * 4 + \
            [5, 9, 14, 20] * 4 + \
            [4, 11, 16, 23] * 4 + \
            [6, 10, 15, 21] * 4

        def F(B, C, D, i):
            if 0 <= i <= 15:
                return (B & C) | ((~B) & D)
            elif 16 <= i <= 31:
                return (D & B) | ((~D) & C)
            elif 32 <= i <= 47:
                return B ^ C ^ D
            elif 48 <= i <= 63:
                return C ^ (B | (~D)) 

        combination = (F(B, C, D, i) + A + words_array[currentIndex] + T) & 0xFFFFFFFF


        def left_rotate(x, amount):
            res = (x << amount) | (x >> (32 - amount))
            return res & 0xFFFFFFFF

        rotated_combination = left_rotate(combination, S[i])

        final_combination = (rotated_combination + B) & 0xFFFFFFFF



        return final_combination

    for i in range(64):
        C_new = b
        D_new = c
        A_new = d
        B_new = combine(a, b, c, d, i, words_array)

        a = A_new
        b = B_new
        c = C_new
        d = D_new


    #??
    #'''
    A = (A + a) & 0xFFFFFFFF
    B = (B + b) & 0xFFFFFFFF
    C = (C + c) & 0xFFFFFFFF
    D = (D + d) & 0xFFFFFFFF

    #'''

    hash_result = A.to_bytes(4, 'little') + \
                  B.to_bytes(4, 'little') + \
                  C.to_bytes(4, 'little') + \
                  D.to_bytes(4, 'little')

    return hash_result.hex()


def printBinary(t):
    i = 0

    for b in t:
        i+=1
        print(format(b, '08b'), end=' ')
        if i == 8:
            print('\n')
            i = 0


def main():

    text = 'abc'

    padded_text = padding(text)

    #printBinary(padded_text)
    resultOfMD5 = MD5(padded_text)

    print(f"RES:  {MD5(padded_text)}")

    #print(resultOfMD5)

main()