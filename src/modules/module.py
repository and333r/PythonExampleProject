"""An example python module"""

from typing import List 
#this is a third-party package. See main.py for instructions on how to install third part packages
import requests 

#Dynamic typing
def total(x,y):
    """Returns the sum of xs"""
    return x + y

#Static typing (really just type hints) see https://docs.python.org/3/library/typing.html
def listTotal(xs: List[float]) -> float:
    result: float = 0.0
    for x in xs:
        result += x
    return result

def getResponseCode():
   r = requests.get("https://www.google.com")
   return r.status_code

def getRequest(url):
    return requests.get(url) 