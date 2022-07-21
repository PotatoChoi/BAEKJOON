C=int(input())
for i in range(C):
    Ticket = list(map(int,input().split()))
    Sub = [Ticket[i] for i in range(1,Ticket[0]+1)]
    Grad = list([1 for i in range(1,Ticket[0]+1) if Ticket[i]>sum(Sub)/Ticket[0]])
    print("{:.3f}%".format((sum(Grad)/Ticket[0])*100))