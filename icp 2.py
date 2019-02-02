
ave = 0
try:
    while True:
        n = input('please input the number')
        s = 0
        for y in input().split():
            s = s + int(y)
            ave = s / int(n)
        print('the average of the number is ', ave)

        s = input('please input a string \n')
        print(s.swapcase())
except EOFError:
    exit()
