"""Exception classes.

    author: Jiu Chang
    email: jiuchang@berkeley.edu
"""

import sys
import random
import json
        
class Error(Exception):
    """Base class for other exceptions"""
    pass

class TooShortError(Exception):
    """Raised when the input value is "" """
    def __init__(self, lower_limit, message="글자 이상이어야 합니다."):
        self.lower_limit = lower_limit
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.lower_limit}{self.message}\n'

class IncorrectLengthError(Exception):
    def __init__(self, id_type, message="자리입니다."):
        self.id_type = id_type
        self.id_name, self.limit = self.set_attributes()
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.id_name}는 {self.limit}{self.message}\n'
    
    def set_attributes(self):
        if self.id_type == "student":
            return ("학생 ID", 17)
        if self.id_type == "parent":
            return ("학부모 ID", 16)

class IncorrectFormat(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}\n'

class NotInRangeError(Exception):
    def __init__(self, limit, lower_limit = 0, message="을(를) 포함해 그 사이에 있는 숫자를 입력하십시오."):
        self.limit = limit
        self.lower_limit = lower_limit
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.lower_limit}과 {self.limit}{self.message}\n'

class NotFoundInDict(Exception):
    def __init__(self, message="No student found in dictionary. Try updating the dictionary or inputing different class names."):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}\n'
