
def add_one_to_input(user_input:str)->str:
    try:
        number = 1 + int(float(user_input.strip()))
    except ValueError:
        print("try using only numerals")
        exit()

    return str(number)

print(add_one_to_input(input("type a number: ")))