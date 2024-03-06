import time
import math

def calculateSquareRoot(number, milliseconds):
    time.sleep(milliseconds/1000.0)
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root} ")

number = int(input())
milliseconds = int(input())
calculateSquareRoot(number, milliseconds)
