
import re
import math


with open("file_name.txt", "rt") as file:
    file_data = file.read()

numbers = map(int, re.findall(r"\b(\d+)\b", file_data))
even = len([number for number in numbers if math.sqrt(number) % 2 == 1])
odd = len([number for number in numbers if math.sqrt(number) % 2 == 0])

print(f"Even: {even}, Odd: {odd}")