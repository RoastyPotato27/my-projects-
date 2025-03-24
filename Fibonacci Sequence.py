# FIBONACCI SQUENCE >

n = int(input("Enter total number of terms: "))

n1,n2 = 0,1 
count = 0

if n <= 0:
    print("Enter positive value.")

elif n == 1:
    print("==========================================")
    print("Fibonacci Sequence for ", n, "term(s) is: ")
    print("==========================================")
    print(n1)

else:
    print("==========================================")
    print("Fibonacci Sequence for ", n, "term(s) is: ")
    print("==========================================")
    while count < n:
        print(n1)
        n3 = n1 + n2

        n1 = n2
        n2 = n3
        count += 1

