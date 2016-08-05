key = [chr(i) for i in range(65, 91)]
playfair = list(''.join(input("Enter the cipher key:").upper().split()))
cipher = []
for i in playfair:
    if i not in cipher:
        cipher.append(i)
        key.remove(i)
cipher.extend(key)
if 'J' in cipher:
    cipher.remove('J')
matrix = []
for i in range(0, 21, 5):
    matrix.append(cipher[i:i + 5])
for i in matrix:
    print(i)


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)


def encrypt():
    ptext = list(''.join(input("Enter plain text to encrypt: ").upper().split()))
    ctext = ""
    print(len(ptext))
    for i in range(0, len(ptext), 2):
        if (i + 1) < len(ptext) and ptext[i] == ptext[i + 1]:
            ptext.insert(i + 1, 'Z')
    if len(ptext) % 2 != 0:
        ptext.append('Z')
    while 'J' in ptext:
        z = ptext.index('J')
        ptext.remove('J')
        ptext.insert(z, 'I')
    for i in range(0, len(ptext), 2):
        r1, c1 = index_2d(matrix, ptext[i])
        r2, c2 = index_2d(matrix, ptext[i + 1])
        if r1 == r2:
            ctext += matrix[r1][(c1 + 1) % 5]
            ctext += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ctext += matrix[(r1 + 1) % 5][c1]
            ctext += matrix[(r2 + 1) % 5][c2]
        else:
            ctext += matrix[r1][c2]
            ctext += matrix[r2][c1]
    ctext = list(ctext)
    print("Encrypted text: ", ''.join(ctext))
    return


def decrypt():
    ctext = list(''.join(input("Enter cipher text to decrypt: ").upper().split()))
    dtext = ""
    for i in range(0, len(ctext), 2):
        r1, c1 = index_2d(matrix, ctext[i])
        r2, c2 = index_2d(matrix, ctext[i + 1])
        if r1 == r2:
            dtext += matrix[r1][(c1 - 1) % 5]
            dtext += matrix[r2][c2 - 1 % 5]
        elif c1 == c2:
            dtext += matrix[(r1 - 1) % 5][c1]
            dtext += matrix[(r2 - 1) % 5][c2]
        else:
            dtext += matrix[r1][c2]
            dtext += matrix[r2][c1]

    print("Decrypted text: ", dtext)
    return


while True:
    print("\n\n\n1.Encryption\n2.Decryption\n---Enter for Exit---")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        break
