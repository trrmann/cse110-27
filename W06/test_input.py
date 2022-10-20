# test_input.py
from types import NoneType
from input import *

#NoneType

case_names = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
results = {}
cases = {}
results[case_names[0]] = input_string("Press Enter:", "Invalid Reply!")
print(f"({results[case_names[0]]})")
cases[case_names[0]] = input("Did it move on?")

results[case_names[1]] = input_string("Type x and press Enter:", "Invalid Reply!")
print(f"({results[case_names[1]]})")
cases[case_names[1]] = input("Did it move on?")

results[case_names[2]] = input_string("Press Enter:", "Invalid Reply!", default_str="default")
print(f"({results[case_names[2]]})")
cases[case_names[2]] = input("Did it move on?")

results[case_names[3]] = input_string("Type x and press Enter:", "Invalid Reply!", default_str="default")
print(f"({results[case_names[3]]})")
cases[case_names[3]] = input("Did it move on?")

results[case_names[4]] = input_string("Press Enter:", "Invalid Reply!", ["T","S"], "default")
results[case_names[4]] = input_string("Press Enter:", "Invalid Reply!", ["T","S"], NoneType)
print(f"({results[case_names[4]]})")
cases[case_names[4]] = input("Did it move on?")
