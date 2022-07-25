T = int(input())
for i in range(T):
    H,W,N = map(int, input().split())
    RoomNumber = (N%H)*100 + (1+(N//H))
    if N%H == 0:
        RoomNumber = (H)*100 + (N//H)
    print(RoomNumber)