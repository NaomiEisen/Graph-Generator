"""
Determine the test version for comparison
Supports only two different versions
"""""
from enum import Enum

class TestVersion(Enum):
    V1 = 0
    V2 = 1