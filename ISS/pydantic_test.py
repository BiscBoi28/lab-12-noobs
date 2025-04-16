from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str | None = None

# Valid data
user1 = User(name="Alice", age=25)
print(user1)  # Should print: name='Alice' age=25 email=None

# Invalid data (should raise ValidationError)
try:
    user2 = User(name="Bob", age="not_an_int")
except ValidationError as e:
    print("Validation Error:", e.json())