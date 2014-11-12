# Write a program that asks users to enter n integers and
# prints the largest odd out of n numbers.


def largestOdd(xlist):
    flag = 1
    maxOdd = None
    for n in xlist:
        if (n % 2 == 1):
            if flag == 1:
                maxOdd = n
                flag == 0
            elif n > maxOdd:
                maxOdd = n
    return maxOdd

st = raw_input("Enter comma separated integers: ")
st = st.strip()
slist = st.split(",")
nums = []
for n in slist:
    i = int(n)
    nums.append(i)

result = largestOdd(nums)

print 'Largest odd is: {}'.format(result)
