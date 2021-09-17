"""Example of a test module"""
#Python and pytest naming convention: notice the suffix {module name}_test.py
from ..src.modules.module import *

#Again notice the naming convention test_{test name}
# -> None means the function doesnt return anything
#In this case the test function doesnt return anything just calls the assert function
def test_total_0() -> None:
    assert total(0,0) == 0

#Notice how -> int test stil passes. Thats because its really just a type hint.
#There for it doesnt affect the way the code is executed. 
#However if using a linter expect it to throw an error
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
    assert getResponseCode() == 200  

#Here is an example of using a mocking framework
#Note before this was done i has to do the following to install the mock package like so
#pip install pytest-mock
def test_can_make_get_request(mocker) -> None:
    
    #Arrange - Arrange the test ie set up mocks and expected outputs
    expectedResult = requests.Response()
    expectedResult.status_code = 200

    #Mock actual call to a website with fake response becuase here we are testing our code, not some external site
    mockedRequest = requests.Response()
    mockedRequest.status_code = 200
    mocker.patch('requests.get', return_value=mockedRequest)

    #Act - Perform some action that will cause some verifiable output to be produced
    actualResult = getRequest('https://doesntexist.secarma.com/')

    #Assert - Check that action has worked as the developer intended. Assert that the expected result is equal to the actual result
    assert actualResult.status_code == expectedResult.status_code
    