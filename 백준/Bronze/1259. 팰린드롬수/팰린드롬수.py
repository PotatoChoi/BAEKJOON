while True:
    a = input()
    if a=="0":
        break
    if (len(a)%2) == 0:
        for i in range(len(a)//2):
            if a[i] == a[-(i+1)]:
                b=1
            else:
                b=0
                break
        if b==1:
            print("yes")
        else:
            print("no")
    else:
        for i in range((len(a)//2)+1):
            if a[i] == a[-(i+1)]:
                b=1
            else:
                b=0
                break
        if b==1:
            print("yes")
        else:
            print("no")
