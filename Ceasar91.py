def cipher(ptext, key):
    ctext = ""
    key %= 26
    for i in ptext:
        if 64 < ord(i) < 91:
            if ord(i) + key > 90:
                print("Ascii", ord(i))
                ctext += chr(ord(i) + key - 26)
                print("ans", ord(i) + key - 26, chr(ord(i) + key - 26))
            else:
                ctext += chr(ord(i) + key)
        else:
            if ord(i) + key > 122:
                ctext += chr(ord(i) + key - 26)
            else:
                ctext += chr(ord(i) + key)
    return ctext


def plain(ctext, key):
    ptext = ""
    key %= 26
    for i in ctext:
        if 64 < ord(i) < 91:
            if ord(i) - key < 65:
                ptext += chr(ord(i) - key + 26)
            else:
                ptext += chr(ord(i) - key)
        else:
            if ord(i) - key < 97:
                ptext += chr(ord(i) - key + 26)
            else:
                ptext += chr(ord(i) - key)
    return ptext


while True:
    print("1.Encryption\n2.Decryption\n3.Exit")
    choice = int(input("Enter Your Choice:(1 or 2)"))
    if choice == 1:
        ptext = input("Enter plain text(only alphabets):")
        key = int(input("Enter key:"))
        if key % 26 == 0:
            print("Error Invalid Key")
        else:
            print(cipher(ptext, key))

    elif choice == 2:
        ctext = input("Enter cipher text(only alphabets):")
        key = int(input("Enter key:"))
        if key % 26 == 0:
            print("Error Invalid Key")
        else:
            ptext = plain(ctext, key)
            print(ptext)
    else:
        break
