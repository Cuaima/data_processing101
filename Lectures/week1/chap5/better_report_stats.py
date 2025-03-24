def farenheitToCelsius(yesterday, change):
    farenheit = float(yesterday) + float(yesterday) * float(change)
    celsius = int(((farenheit - 32) * 5) / 9)
    return "The current weather is " + str(celsius) + "C (" + str(farenheit) + "F)."

yesterday = input("temp yesterday(in integers or floats): ")
change = input("change(in integers or floats): ")
print(farenheitToCelsius(yesterday, change))