limit = 10
number = 0
result = 0

number = int(input("Enter a number for its table: "))
for i in range(1, limit + 1):
    result = number * i
    print(str(number) + " * " + str(i) + " = " + str(result))
