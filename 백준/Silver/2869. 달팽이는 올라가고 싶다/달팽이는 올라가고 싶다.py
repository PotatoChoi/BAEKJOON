A, B, V = map(int, input().split())
Day = (V-B)/(A-B)
if int(Day)<Day:
    Day += 1

Day = int(Day)
print(Day)