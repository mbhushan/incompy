# print the cube root of an integer if it exists.
# if the input is not a perfect cube, it prints a msg to that effect

num = int(raw_input("Enter integer: "))
ans = 0
while ans**3 < abs(num):
    ans += 1

if ans**3 > abs(num):
    print '{} is not a perfect cube'.format(num)
else:
    if num < 0:
        ans = -ans
    print 'cube root of {} is {}'.format(num, ans)
