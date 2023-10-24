a = input("Enter the change you have made : ")
print(f'The change i made is given as : {a}')

n = int(input("Enter the number : "))
def fizzbuzz(n):
    for i in range(1,n+1):
        if (i % 3 == 0) or (i % 5 == 0):
            print('Fizzbuzz')
        else:
            print(i)

print(fizzbuzz(n))