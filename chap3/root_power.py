# write a program that asks user to enter an integer i and we print 2 integers
# of the form root and pwr such that root**pwr = i where 0 < pwr < 6

num = int(raw_input("Enter an integer: "))

root = 1
pwr = 1
flag = 0
for i in range(2, 6):
    while root**i < num:
        root += 1
    if root**i == num:
        pwr = i
        flag = 1
        break
    root = 1

if flag == 1:
    print 'root**pwr combination exists for {}'.format(num)
    print 'root: {}, pwr: {}'.format(root, pwr)
else:
    print 'NO combination of root**pwr exists!!'
