# 03习题
def collatz(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        result = number // 2
        print(number, "// 2 =", result)
        collatz(result)
    else:
        result = number * 3 + 1
        print(number, "* 3 + 1 =", result)
        collatz(result)

try:
    number = int(input("Please input your number:"))
except ValueError:
    print("Please input Integer!!!")
else:
    result = collatz(number)

