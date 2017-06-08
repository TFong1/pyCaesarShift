'''
Cyber League Competition Caesar's Shift Password Cracker
Written by Tony Fong
'''

'''
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
'''
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

'''
ENCRYPTEDWORD = "ybfrnterrq"
ENCRYPTEDWORD = "qernzsrrypbbx"
ENCRYPTEDWORD = "gpxhtsgdrz"
ENCRYPTEDWORD = "zluzlOhchuh"
ENCRYPTEDWORD = "negvpyrfgnaq"
ENCRYPTEDWORD = "pdqqhuvwrs"
ENCRYPTEDWORD = "orggrenavznyzrzore"
'''

ENCRYPTEDWORD = "RGQT"

numIterations = len(ALPHABET)

for shift in range(0, numIterations):
    print("{:>2}: ".format(shift+1), end='')
    for c in ENCRYPTEDWORD:
        print(ALPHABET[(ALPHABET.index(c) + shift) % numIterations], end='')

    print()
