"""Example of a test module"""
#Python and pytest naming convention, notice the suffix {module name}_test.py

#To run tests open vs terminal and enter the command: python -m pytest /optional path tot file/ 
#Alternatively, to run tests using vs code test explorer
#First enable testing, use the "Python: Configure Tests" command on the Command Palette (ctrl + alt + p)
#Next on the command pallet use the command Python: Discover Tests. 
#This should load the vscode test explorer in the right hand pannel. Its icon is a test flask
#When running tests and they fail, hover over the failing test code and an alert box should tell you whats failing and why
#For more error info run the tests using the terminal

from ..src.modules.module import *

#Again notice the naming convention test_{test name}
# -> None means the function doesnt return anything
#In this case the test function doesnt return anything just calls the assert function
def test_total_0() -> None:
    assert total(0,0) == 0

#Notice how -> int test stil passes. Thats because its really just a type hint.
#There for it doesnt affect the way the code is executed. 
#However using a linter i expect it to throw an error
def test_total_1() -> int:
    assert total(0,1) == 1

def test_total_3():
    assert total(1,2) == 3

def test_total_4():
    assert total(1,3) == 4

def test_total_minus4():
    assert total(0,-4) == -4

def test_list_total_None() -> None:
    assert listTotal([]) == 0

def test_list_total_6() -> None:
    assert listTotal([1.0,2.0,3.0]) == 6.0

def test_can_use_third_party_package() -> None:
    assert makeRequest() == 200  

    