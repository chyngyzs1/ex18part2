age = int(input('vedite vash vozrast:'))
if age % 2 == 0:
    for i in range(2, age+1):
        if i % 2 == 0:
            print(i)
        else:
            pass
if age % 2 == 1:
    for i in range(1 , age+1):
        if i % 2 == 1:
            print(i)
        else:
            pass