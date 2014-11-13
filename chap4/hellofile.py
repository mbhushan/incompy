# simple file write operation

f = open('kids.txt', 'w')

for i in range(3):
    st = raw_input('Enter name: ')
    f.write(st + '\n')

f.close()
