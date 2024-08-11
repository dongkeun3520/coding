

for _ in range(1000):
    # if map(int,input().split()) == (0,0,0):
    #     break
    blank = list(map(int,input().split()))
    blank.sort()

    if blank[0] == 0:
        break
    if blank[0] + blank[1] <= blank[2]:
        print("Invalid")
    else:
        if blank[0] == blank[1] and blank[1] == blank[2] and blank[0] == blank[2]:
            print("Equilateral")
        else:
            if blank[0] != blank[1] and blank[1] !=blank[2] and blank[0] != blank[2]:
                print("Scalene")
            else:
                print("Isosceles")
