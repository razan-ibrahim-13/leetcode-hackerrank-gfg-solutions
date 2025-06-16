# Task: Print the numbers from 1 to n in a single line without spaces.
# Input Format
# n=5
# Print the string : 12345

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i,end='')