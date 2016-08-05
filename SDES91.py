key1 = int('00101111', 2)
key2 = int('11101010', 2)
s0 = {0: [1, 0, 3, 2], 1: [3, 2, 1, 0], 2: [0, 2, 1, 3], 3: [0, 1, 3, 2]}
s1 = {0: [0, 1, 2, 3], 1: [2, 0, 1, 3], 2: [3, 0, 1, 0], 3: [2, 1, 0, 3]}


def f(r, key):
    rList = list("{0:04b}".format(r))
    p1 = [4, 1, 2, 3, 2, 3, 4, 1]
    r1 = [rList[x - 1] for x in p1]
    r1 = int("{0:08b}".format(int(''.join(r1), 2)), 2)
    r1 = r1 ^ key
    rList = list("{0:08b}".format(r1))
    r1 = int(rList[0] + rList[3], 2)
    c1 = int(rList[1] + rList[2], 2)
    r2 = int(rList[4] + rList[7], 2)
    c2 = int(rList[5] + rList[6], 2)
    ans = "{0:02b}".format(s0[r1][c1]) + "{0:02b}".format(s1[r2][c2])
    ansList = list(ans)  # list of ans
    p2 = [2, 4, 3, 1]
    ans = [ansList[x - 1] for x in p2]
    ans = int("{0:04b}".format(int(''.join(ans), 2)), 2)
    return ans


def f1(l, r):
    a = f(r, key1)
    temp = l ^ a
    ans1 = "{0:04b}".format(temp)
    ans2 = "{0:04b}".format(r)
    return ans1, ans2


def f2(l, r):
    a = f(r, key2)
    temp = l ^ a
    ans1 = "{0:04b}".format(temp)
    ans2 = "{0:04b}".format(r)
    return ans1, ans2


def initP(i):
    ipList = "{0:08b}".format(i)
    ipList = list(ipList)  # list of ip
    p1 = [2, 6, 3, 1, 4, 8, 5, 7]
    i = [ipList[x - 1] for x in p1]
    i = int("{0:08b}".format(int(''.join(i), 2)), 2)
    return i


def finalP(o):
    ipList = list("{0:08b}".format(int(o, 2)))
    p1 = [4, 1, 3, 5, 7, 2, 8, 6]
    o = [ipList[x - 1] for x in p1]
    o = int("{0:08b}".format(int(''.join(o), 2)), 2)
    return o


def encryption():
    ip = int(input("Enter Plain Text to Encrypt:"), 2)
    ip = initP(ip)  # ip for input
    l = int("{0:08b}".format(ip)[0:4], 2)
    r = int("{0:08b}".format(ip)[4:8], 2)
    lTemp, rTemp = f1(l, r)
    lTemp = int(lTemp, 2)
    rTemp = int(rTemp, 2)
    lans, rans = f2(rTemp, lTemp)
    op = lans + rans
    op = finalP(op)  # op for output
    print("Encrypted Text :", "{0:08b}".format(op))


def decryption():
    ip = int(input("Enter Encrypted Text to Decrypt:"), 2)
    ip = initP(ip)
    l = int("{0:08b}".format(ip)[0:4], 2)
    r = int("{0:08b}".format(ip)[4:8], 2)
    ltemp, rtemp = f2(l, r)
    ltemp = int(ltemp, 2)
    rtemp = int(rtemp, 2)
    lans, rans = f1(rtemp, ltemp)
    op = lans + rans
    op = finalP(op)
    print("Plain Text :", "{0:08b}".format(op))


while True:
    choice = input("\n\n\n1.Encryption\n2.Decryption\n----Anything Else For Exit----\nEnter your Choice:")
    if choice == '1':
        encryption()
    elif choice == '2':
        decryption()
    else:
        break
