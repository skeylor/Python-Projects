def brute():
    x = 1
    while x < 5:
        x = round(x,3)
        if 7.5 + 1.5 * x == 10.4:
            print('answer =',x)
            return
        else:
            print(x,7.5 + 1.5 * x)
        x += .001

brute()
            