"""
Write a script report_stats.py that starts with the following information: 
- the temperature for yesterday represented as an int (40), 
- the relative change in temperature weather for today (compared to yesterday) represented as a float (0.4). 
- These temperature units are in degrees Farenheit. To convert to Celcius, you can use the equation: 
 
Using all this information, display a message in the VSCode terminal that reads the following exactly (including inaccuracies), where the Celcius conversion is done using the equation above:
The current weather is 13C (56F).
"""

def farenheitToCelsius(yesterday, change):
    farenheit = yesterday + yesterday * change
    celsius = int(((farenheit - 32) * 5) / 9)
    return "The current weather is " + str(celsius) + "C (" + str(farenheit) + "F)."

print(farenheitToCelsius(40, 0.4))