#1. rocket launch
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
    else:
        print("Launch!")
count=5
countdown(count)

#2. fibonnaci series
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

#3. factorial
def factorial(n):
    if n==0:
        return 1;
    else:
        return n*factorial(n-1)
print(factorial(999))

#4.bank
def p_power(p, n):
    if n == 0:
        return 1
    else:
        return p * p_power(p, n - 1)
p = 3
n = 4
result = p_power(p, n)
print(f"{p}^{n} = {result}")

#5. HR department
def id_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
         return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
            return 1;
n=int(input("enter no.of employees"))
arr=[]
print('enter no.of employees in sorted order:')
if arr==sorted(arr):
    print('\n the input list is already sorted')
else:
        print('\n the input list is not sorted')
        print('\nsorting the list....')
        arr.sort()
        print('sorted list',arr)
for i in range(n):
    arr.append(int(input()))
    key=int(input('enter the employee to search:'))
    result=id_search(arr,key)
    if result!=-1:
        print('employee not found')
    else:
        print('employee found')
        #lab 1 completed
