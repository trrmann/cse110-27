# test_input.py
import sys
import os
from types import NoneType
from input import *

class Test:
    inFileName = "test_input.txt"
    outFilename = "test_output.txt"

    def test_function(self, functionDictionary, functionName, *arguments, stdin_input):
        results = {}
        Test.setup_method(stdin_input)
        results["input"] = arguments
        results["output"] = functionDictionary.get(functionName)(*arguments)
        Test.teardown_method()
        results["std_input"] = Test.get_input()
        results["std_output"] = Test.get_output()
        Test.cleanup()
        return results

    def setup_method(self, stdin_input):
        if os.path.exists(self.outFilename):
            os.remove(self.outFilename)
        test_in_file = open(self.inFileName, "w")
        test_in_file.write(stdin_input)
        test_in_file.close()
        self.orig_stdin = sys.stdin
        self.orig_stdout = sys.stdout
        sys.stdin = open(self.inFileName)
        sys.stdout = open(self.outFilename, "w")

    def teardown_method(self):
        sys.stdin = self.orig_stdin
        sys.stdout = self.orig_stdout
        self.outFilename.close()

    def get_input(self):
        test_in_file = open(self.inFilename)
        input = test_in_file.read()
        test_in_file.close()
        return input

    def get_output(self):
        test_out_file = open(self.outFilename)
        output = test_out_file.read()
        test_out_file.close()
        return output

    def cleanup(self):
        if os.path.exists(self.inFileName):
            os.remove(self.inFileName)
        if os.path.exists(self.outFilename):
            os.remove(self.outFilename)


#NoneType


input_string("Press Enter:", "Invalid Reply!")

case_names = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
results = {}
cases = {}
results[case_names[0]] = input_string("Press Enter:", "Invalid Reply!")
#print(f"({results[case_names[0]]})")
#cases[case_names[0]] = input("Did it move on?")

#results[case_names[1]] = input_string("Type x and press Enter:", "Invalid Reply!")
#print(f"({results[case_names[1]]})")
#cases[case_names[1]] = input("Did it move on?")

#results[case_names[2]] = input_string("Press Enter:", "Invalid Reply!", default_str="default")
#print(f"({results[case_names[2]]})")
#cases[case_names[2]] = input("Did it move on?")

#results[case_names[3]] = input_string("Type x and press Enter:", "Invalid Reply!", default_str="default")
#print(f"({results[case_names[3]]})")
#cases[case_names[3]] = input("Did it move on?")

#results[case_names[4]] = input_string("Press Enter:", "Invalid Reply!", ["T","S"], "default")
#results[case_names[4]] = input_string("Press Enter:", "Invalid Reply!", ["T","S"], NoneType)
#print(f"({results[case_names[4]]})")
#cases[case_names[4]] = input("Did it move on?")
