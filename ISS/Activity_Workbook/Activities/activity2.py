'''
TASK: Understanding pydantic models
'''

# importing the necessary classes from pydantic to create a model
from pydantic import BaseModel,ValidationError
from typing import Optional

# creating a base model, with 3 elements, id(int),name(str) and an optional
# parameter called age which is of type int
class User(BaseModel):
    id : int
    name : str 
    age : Optional[int] = None

#case 1  
user_data={
    "id": 1,
    "name": "Narain",
    "age": 21
}

# this piece of code checks if case 1 is a valid data from User model
try:
    user=User(**user_data)
    print(user)
except ValidationError as e:
    print("Validation Error:",e)
    
#case 2    
user_data={
    "id": 1,
    "name": "Narain"
}

# this piece of code checks if case 2 is a valid data from User model
try:
    user=User(**user_data)
    print(user)
except ValidationError as e:
    print("Validation Error:",e)

#case 3
user_data={
    "id": "abc",
    "name": "Narain"
}

# this piece of code checks if case 3 is a valid data from User model
try:
    user=User(**user_data)
    print(user)
except ValidationError as e:
    print("Validation Error:",e)