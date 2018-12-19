'''
So you think you can HACK?

Given the plaintext and the ciphertext produced using Playfair Cipher. Deduce the key. To make things simpler for you, consider that the English alphabets start with A and end with I.

Input
The input consists of 2 lines. The first line is a string that represents the plaintext which consists of capital English alphabetical letters between A and I. The length of the string would not exceed 10. The second line is a string that represents the ciphertext. It will be of same size as the plaintext(i.e: while encrypting, you never needed to insert an extra character.) The string also consists of capital English alphabetical letters between A and I.

Output
The output should be a single line that represents the key(9 characters) that was used to encrypt the plaintext and produced the given ciphertext. Since there would definitely be many solutions, print the lexicographically smallest one. i.e: If you have 2 solutions, one of them the A comes before the B and the second one, the B comes before the A, you should output the first one.

input:
ICED
CFFE
output:
ABCDEFGHI
'''

import itertools
from collections import OrderedDict
rmChar = lambda c, arr : arr.replace(c,'')
alpha = 'ABCDEFGHI'

def indexOfChar(c, mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == c:
                return i,j

def charInSameRow(a,b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)
    return [mat[i1][0] if j1==2 else mat[i1][j1+1], mat[i2][0] if j2==2 else mat[i2][j2+1]]

def charInSameCol(a,b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)

    return [mat[0][j1] if i1==2 else mat[i1+1][j1], mat[0][j2] if i2==2 else mat[i2+1][j2]]
def charInDiff(a, b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)
    return [mat[i1][j2], mat[i2][j1]]

def orchestrator(a, b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)
    if i1 == i2:
        return charInSameRow(a, b, mat)
    elif j1 == j2:
        return charInSameCol(a, b, mat)
    return charInDiff(a, b, mat)

def fillMat(key):
    alp = alpha
    key = ''.join(list(key))
    for c in key:
        alp = rmChar(c, alp)
    mat_flat = key+alp
    mat = [list(mat_flat[i:i + 3]) for i in range(0, len(mat_flat), 3)]
    return mat

def pphack(msg, cipher):
    stuff = list(alpha)
    randon_keys = list(itertools.permutations(stuff,9))
    for key in randon_keys:
        mat = fillMat(key)
        cipher_2d = [orchestrator(msg[i],msg[i+1], mat) for i in range(0,len(msg),2)]
        estimated_cipher = ''.join([j for sub in cipher_2d for j in sub])
        if cipher == estimated_cipher:
            return ''.join(list(key))

msg = input()
cipher = input()
key = pphack(msg, cipher)
print(key)