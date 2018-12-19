'''
Caesar Cipher

The Caesar cipher, also known as a shift cipher, is one of the simplest forms of encryption. It is a substitution cipher where each letter in the original message (called the plaintext) is replaced with a letter corresponding to a certain number of letters up or down in the alphabet.

In this way, a message that initially was quite readable, ends up in a form that can not be understood at a simple glance.

Let's take for example the string: HACKINGZIBRAS If you choose your key to be 3, each of the letters will be shifted by three characters. So, the encrypted message you get is: KDFNLQJCHEUDV

You can try different messages with different keys in this website: https://www.dcode.fr/caesar-cipher

Your mission now is to implement this yourself.

Input
The input consists of 2 lines. The first line is just a number N ( 0 ≤ N ≤ 99999999999 ) which represents the key that is also the number of right shifts. The second line is a string which represents the plain text. It consists of only capital English letters. i.e: Each character of the string is between A-Z inclusive. No spaces, no special characters and no small letters.

Output
Your output should be the cipher text produced by Ceaser cipher explained above.

input:
3
HACKINGZEBRAS
output:
KDFNLQJCHEUDV
'''
def caesar(key, message):
    key = key%26
    p_ord = [ord(c)+key for c in message]
    cipher = ''.join([chr(p) if p <= 90 else chr(p-26) for p in p_ord])
    return cipher

key = int(input())
plainText = input()
cipher = caesar(key, plainText)
print(cipher)