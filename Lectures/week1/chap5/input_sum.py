user_input1 = input("Number 1: ")
user_input2 = input("Number 2: ")

try:
    number = int(float(user_input2.strip())) + int(float(user_input1.strip()))
except ValueError:
    print("try using only numerals")
    exit()

print(str(number))