name = 'anybody'
while True :
    name, age, waight = map(str, input().split())
    age, waight = int(age), int(waight)
    if name == '#' :
        break
    if age > 17 or waight >= 80 :
        print(f'{name} Senior')
    else :
        print(f'{name} Junior')