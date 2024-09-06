a = []
n = int(input("Enter How many powers of 2 you want to check for Mersenne Primes: "))
i = 4
x = 0


while len(a)<=n:
    a.append(i-1)
    i = i * 2


while x <= len(a) - 1:
    mer_pr = a[x]
    counter = 0
    j = 1

        
    while j <= mer_pr/2:
        if mer_pr%j == 0:
            counter = counter + 1
            j = j + 1
        else:
            j = j + 1


    if counter<=2:
        print(mer_pr, "It is a Mersanne prime number")
    else:
        print(mer_pr, "It is not a Mersanne prime number")    
    
    x = x + 1