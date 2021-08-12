import sys

n = int(sys.argv[1])

if n % 2 == 1:

    print("weird")

elif n >= 2 and n <= 5:

    print("Not weird")

elif n >= 6 and n <= 20:

    print("Weird")

elif n >= 20:

    print("Not Weird")
    
#n % y = remainder(x / y)
