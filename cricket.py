import random


def mainrun():
    run = random.randint(1, 6)
    return run


print("")
print(
    "DISCRIPTION :\n=> Welcome to CracyCrik\n=> CracyCrik Just like Hand Cricket\n=> Number of Overs & Players Your Choice\n=> Enter Number (1-6) to scoring\n=> Computer score automatically generated  \n=> if Entered number & Computer score are same 'GAME OVER'")
print("")

name = input("Enter Your Name : ")
print("<<< Welcome to CrazyCrik,", name, ">>>")
print("")

o = int(input("Enter Number of Overs : "))
play = True
p = 0
while play:
    p = int(input("Enter Number of Players : "))
    if p > 11:
        print("<<< PLAYERS LIMIT - 11 >>>")
    else:
        play = False

print("")

a = {}
for i in range(p):
    print("Enter Name Player ", i + 1, ":")
    a[i] = input()
print("")
print("Enter Number (1-6) to play")
print("")
print("<<< Let's Play Your First Ball >>>")

score = {}
for x in range(p):
    score[x] = 0

total = 0
wic = 0
for j in range(o):
    if wic < p - 1:
        print("OVER :", j + 1)
        for i in range(6):
            if wic < p - 1:
                run = mainrun()
                print("[", j, ".", i + 1, "]")
                A = int(input(" "))
                while A>6:
                    print("INVALID RUN , Enter : 1 - 6 only")
                    print("")
                    print("[", j, ".", i + 1, "]")
                    A = int(input(" "))

                if wic == 0:
                    score[0] += A
                    total += A
                    if A != run:
                        print(a[0], ": ", score[0])
                        print("SCORE/WIC : ", total, "/", wic)
                        print("")
                    if A == run:
                        score[0] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[0], ": ", score[0])
                        print("SCORE/WIC : ", total, "/", wic)
                        print("")

                elif wic == 1:
                    score[1] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[1], ": ", score[1])
                        print("SCORE : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[1] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[1], ": ", score[1])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 2:
                    score[2] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[2], ": ", score[2])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[2] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[2], ": ", score[2])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 3:
                    score[3] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[3], ": ", score[3])
                        print("SCORE : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[3] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[3], ": ", score[3])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 4:
                    score[4] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[4], ": ", score[4])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[4] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[4], ": ", score[4])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 5:
                    score[5] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[5], ": ", score[5])
                        print("SCORE : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[5] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[5], ": ", score[5])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 6:
                    score[6] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[6], ": ", score[6])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[6] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[6], ": ", score[6])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 7:
                    score[7] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[7], ": ", score[7])
                        print("SCORE : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[7] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[7], ": ", score[7])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 8:
                    score[8] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[8], ": ", score[8])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[8] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[8], ": ", score[8])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

                elif wic == 9:
                    score[9] += A
                    total = total
                    total += A
                    if A != run:
                        print(a[9], ": ", score[9])
                        print("SCORE : ", total, "/", wic)
                        print(" ")
                    if A == run:
                        score[9] -= A
                        total -= A
                        print(" ")
                        print("IT'S WICKET...!!!")
                        wic += 1
                        print(a[9], ": ", score[9])
                        print("SCORE/WIC : ", total, "/", wic)
                        print(" ")

print(" ")
for z in range(p):
    print(a[z], ":", score[z])

print("YOUR TOTAL : ", total, "/", wic)
print("")

print("<<< Let's Start Your Bowling >>>")
print("")

a = {}
for i in range(p):
    a[i] = "Player ", i+1


cscore = {}
for x in range(p):
    cscore[x] = 0

ctotal = 0
cwic = 0
for j in range(o):
    if ctotal <= total:
        if cwic < p - 1:
            print("OVER :", j + 1)
            for i in range(6):
                if ctotal <= total:
                    if cwic < p - 1:
                        run = mainrun()
                        print("[", j, ".", i + 1, "]")
                        A = int(input(" "))
                        while A > 6:
                            print("INVALID RUN , Enter : 1 - 6 only")
                            print("")
                            print("[", j, ".", i + 1, "]")
                            A = int(input(" "))

                        if cwic == 0:
                            cscore[0] += A
                            ctotal += A
                            if A != run:
                                print(a[0], ": ", cscore[0])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print("")
                            if A == run:
                                cscore[0] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[0], ": ", cscore[0])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print("")

                        elif cwic == 1:
                            cscore[1] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[1], ": ", cscore[1])
                                print("SCORE : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[1] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[1], ": ", cscore[1])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 2:
                            cscore[2] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[2], ": ", cscore[2])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[2] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[2], ": ", cscore[2])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 3:
                            cscore[3] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[3], ": ", cscore[3])
                                print("SCORE : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[3] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[3], ": ", cscore[3])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 4:
                            cscore[4] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[4], ": ", cscore[4])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[4] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[4], ": ", cscore[4])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 5:
                            cscore[5] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[5], ": ", cscore[5])
                                print("SCORE : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[5] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[5], ": ", cscore[5])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 6:
                            cscore[6] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[6], ": ", cscore[6])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[6] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[6], ": ", cscore[6])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 7:
                            cscore[7] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[7], ": ", cscore[7])
                                print("SCORE : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[7] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[7], ": ", cscore[7])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 8:
                            cscore[8] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[8], ": ", cscore[8])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[8] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[8], ": ", cscore[8])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

                        elif cwic == 9:
                            cscore[9] += A
                            ctotal = ctotal
                            ctotal += A
                            if A != run:
                                print(a[9], ": ", cscore[9])
                                print("SCORE : ", ctotal, "/", cwic)
                                print(" ")
                            if A == run:
                                cscore[9] -= A
                                ctotal -= A
                                print(" ")
                                print("IT'S WICKET...!!!")
                                cwic += 1
                                print(a[9], ": ", cscore[9])
                                print("SCORE/WIC : ", ctotal, "/", cwic)
                                print(" ")

print(" ")
for z in range(p):
    print(a[z], ":", cscore[z])

print("COMPUTER TOTAL : ", ctotal, "/", cwic)
print("")

if total>ctotal:
    print("YOU ARE THE WINNER...!")
elif total<ctotal:
    print("THE WINNER IS COMPUTER...!")
elif total==ctotal:
    print("MATCH DRAW")