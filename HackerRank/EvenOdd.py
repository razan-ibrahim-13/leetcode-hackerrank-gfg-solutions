n = int(input())

if (n%2==0):
    if (2<n<5):
        print("Not Weird")
    elif (n>20):
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")