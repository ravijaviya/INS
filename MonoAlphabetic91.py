seq = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def generate():
    from random import shuffle
    shuffle(seq)
    print("key generated...")
    return


def cipher():
    ptext = input("Enter Plain Text:")
    text = plain = ctext = ""
    text = ptext.upper().split()
    for i in text:
        plain += i
    for i in plain:
        ctext += seq[ord(i) - 65]
    print(ctext)
    return


def decipher():
    ctext = input("Enter Cipher Text:")
    text = ci = plain = ""
    text = ctext.upper().split()
    for i in text:
        ci += i
    for i in ci:
        plain += chr(seq.index(i) + 65)
    print(plain)
    return


while True:
    print("\n\n\n1.Encryption\n2.Decryption\n3.Generate New Key\n4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        cipher()
    elif choice == 2:
        decipher()
    elif choice == 3:
        generate()
    else:
        break
