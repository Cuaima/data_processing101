def from_str_to_avg(object1, object2, object3):
    try: 
        number1 = float(object1)
        number2 = float(object2)
        number3 = float(object3)
    except:
        print("that item is not a number")
    
    average = (number1 + number2 + number3) / 3
    return average

print(from_str_to_avg("2", "5", "8"))