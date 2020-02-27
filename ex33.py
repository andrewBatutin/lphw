i = 0
numbers = []

def incr_while(s, n):
    i = 0
    while i < n:
        print ("At the top i is %d" % i)
        numbers.append(i)

        i = i + s
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d" % i)

def incr_loop(n):
    for i in range(0,n):
        print(i)

print ("The numbers: ")

for num in numbers:
    print (num)

incr_while(2,10)
incr_loop(10)
