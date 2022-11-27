t = input()

for i in range(int(t)):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError,ValueError) as e:
        print('Error Code:',e)
