'''
Playfair Cipher

You are already familiar with playfair so lets handle the special cases.

You handle J as I.
When two characters are in the same row, you take the one on the right.
When two characters are in the same column, you take the one below.
If you end up with one letter, you append 'X' since it is slightly used in all languages and almost never coupled with another 'X'.
When two characters are the same, You separate them with 'X'
If you get two consecutive 'X' ('XX') you separate them by the second least used character which is 'Q'
You can play with reference algorithm at http://www.online.crypto-it.net/eng/playfair.html

Warning: The website is a playground to understand how things work. The website uses 'Q' rather than 'X' and 'V' rather than 'Q' so don't copy his solution.

Input
2 lines. The first is the Key with Length > 0 The second is the plain text with Length > 0 All inputs are Uppercase letters with no spaces or special characters.

Output
1 line containing the cipher text.

input:
KEYWORD
BALLOON
output:
CBIZSCES
input:
AECUSR
MEETINGS
output:
ISSOHOMG
'''
import itertools
from collections import OrderedDict
rmChar = lambda c, arr : arr.replace(c,'')
alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def indexOfChar(c, mat):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == c:
                return i,j

def charInSameRow(a,b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)
    return [mat[i1][0] if j1==4 else mat[i1][j1+1], mat[i2][0] if j2==4 else mat[i2][j2+1]]

def charInSameCol(a,b, mat):
    i1, j1 = indexOfChar(a, mat)
    i2, j2 = indexOfChar(b, mat)
    return [mat[0][j1] if i1==4 else mat[i1+1][j1], mat[0][j2] if i2==4 else mat[i2+1][j2]]

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

def cleanMsg(msg):
    msg = msg.replace('J','I')
    msg = list(msg)
    for i in range(0,len(msg),2):
        if not i==len(msg)-1:
            if msg[i] == msg[i+1]:
                if msg[i] == 'X':
                    msg.insert(i+1, 'Q')
                else:
                    msg.insert(i+1, 'X')
    if len(msg) % 2 == 1:
        msg.append('Q') if msg[-1]=='X' else msg.append('X')
    return msg

def fillMat(key):
    alp = alpha
    for c in key:
        alp = rmChar(c, alp)
    mat_flat = key+alp
    mat = [list(mat_flat[i:i + 5]) for i in range(0, len(mat_flat), 5)]
    return mat

def cleanKey(key):
    key = key.replace('J','I')
    key = ''.join(OrderedDict.fromkeys(key).keys())
    return key

def playfair(key, message):
    key_cleaned = cleanKey(key)
    mat = fillMat(key_cleaned)
    msg = cleanMsg(message)
    cipher_2d = [orchestrator(msg[i],msg[i+1], mat) for i in range(0,len(msg),2)]
    cipher = ''.join([j for sub in cipher_2d for j in sub])
    return cipher    

key = input()
msg = input()
cipher = playfair(key, msg)
print(cipher)