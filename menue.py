while True:
    print("a)game number")
    print("b)score game")
    print("c)game stars")
    x=input("choose a game")
    match x:
        case "a":
            import random
            j=random.randint(1,100)
            print("adad  madnazar>>")
            while True:
                g=int(input("adad moresnazar shoma?>>"))
                if g<j:
                    print("bozorgtar>>")
                elif g>j:
                    print("kigik tar>>")
                elif g==j:
                    print("WooooooooW")
                elif g<1 or g>100:
                    print("over range")
        case "b":
            bord=0
            mosavi=0
            bakht=0
            total=0
            count=0
            while True:
                a=int(input("emtiaz bazi>>"))
                if a==3:
                    bord+=1
                    total+=3
                    count+=1
                elif a==1:
                    mosavi+=1
                    total+=1
                    count+=1
                elif a==0:
                    bakht+=1
                    total+=0
                    count+=1
                if count==30:
                    break
            print("bord=",bord)
            print("mosavi",mosavi)
            print("bakht",bakht)
            print("total score",total)
        case "c":
            print("a)game satr 1")
            print("b)game star 2")
            x=input("choose your game star>>")
            match x:
                case "a":
                    for i in range(6):
                        for k in range(i):
                            print("*",end=" ")
                        print( )
                case "b":
                    for i in range(6):
                        for k in range(5-i,0,-1):
                            print(" ",end="")
                        for g in range(i):
                            print("*",end="")
                        print( )